## Custom Widget for Checkboxes

### The Problem
I will admit up front that the real problem here is that I have one model that is representing two very similar things that will soon be two different models. One of things is something that can have 0-1 occurrences while the other can have 0+ occurrences. So I wanted two different views to interact with these one having a form that would allow the user to check if the first one is present and another view to say how many of the second were present. So I set up modelforms for both but when I tried to use a checkbox widget for the first I started to run into issues.

The checkbox widget returns True or False which I had hoped would allow me to rely on truthiness to get a 1 or 0 into the model. Well the checkbox widget was written well enough to prevent it being used with fields that are not booleans. After a while on stack overflow and reading the Django documentation I finally understood the issues. I couldn't do anything to clean the value because during the validation phase of saving the form the widget would throw an error and the data would get dropped before I had the chance to do anything with it. I went down a couple rabbit holes that ended up being dead ends (and I am probably better off that they were) but eventually found my solution.

### The Solution
I finally ended up in the source code for the CheckboxInput widget to see how it works. In there is a method call value_from_datadict that is used to transform the values that it gets from request.POST into what the database needs. First it checks for missing values that the HTML doesnt send for unchecked boxes and returns False and then if it does have a value it returns True or False accordingly. So quite easily I was able to make a new widget that I called IntCheckboxInput that does exactly the same as the original CheckboxInput but returns a 1 or 0 instead of True or False.

```python
class IntCheckboxInput(CheckboxInput):
    def value_from_datadict(self, data, files, name):
        if name not in data:
            # A missing value means False because HTML form submission does not
            # send results for unselected checkboxes.
            return 0
        value = data.get(name)
        # Translate true and false strings to boolean values.
        values = {'true': True, 'false': False}
        if isinstance(value, six.string_types):
            value = values.get(value.lower(), value)
        return int(bool(value))
```

Now the form would put the proper value into the database for me. However I ended up with a new problem. Whereas the CheckboxInput was not able to put values into my database it was able to read the integers out of the database and turn the checkbox on if the value wasnt 0. But my new widget was defaulting with the value off all the time. I traced the issue to the check_test of the widget. So the new check_test below looks for 0s instead of false values and everything works great.

```python
def int_test(v):
    return not (v is 0 or v is None or v == '')
```

So now I can use `self.fields['count'].widget = IntCheckboxInput(check_test=int_test)` to create a checkbox that works with integers instead of Booleans. The next thing I am going to do is get rid of all of it and just go fix my models like I should have in the first place but I am really glad that I spent two hours pushing the boundaries of what I could do with Django.