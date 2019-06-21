# Y2 2019 Summer: Routing Lab

Welcome to the routing lab! Please read all the instructions so you don't
get lost halfway through, but definitely feel free to ask for help if you
get stuck. Good luck, and have fun!

### Setup

Before you start coding, make sure you fork and clone the repository
for this lab:
```
cd ~/Desktop
git clone https://github.com/YOUR_GITHUB_USERNAME/y2s19-routing.git
```

## Warm-up Exercises

### Part 1: Basic routing

In `app.py`, change the route for `/` to display the `home.html`
template. You can open `home.html` in Sublime to see what the template
looks like. Remember that templates are in the `templates` folder!

*Hint*: Remember to use the function `render_template`.

You can go back to the command line now and start the server, using
`python app.py`. In the browser, go to `http://127.0.0.1:5000` to
see what it looks like so far.

### Part 2: Variable Routes

In `app.py`, make a new route with two parts: the first part is 
`/student` and the second part will be a variable integer.
The function for this route should be called `display_student(student_id)`. 
When you navigate to `http://127.0.0.1:5000/student/4`, 
for example, the variable `student_id` will be 4.

Then make the function return the rendered template 'student.html'. 
This template has a variable `id_number` which you should make equal 
to `student_id`. If you get stuck, look at the hints.

*Hint*: The variable `student_id` should have type `int`.

*Hint*: For the route you want something like:
@app.route('/student/<int:student_id>')

*Hint*: To render the template, you can do this:
render_template('student.html', id_number=student_id)

### Part 3: URL Building

In `student.html`, add a link to the home page.

*Hint*: Remember how to use `url_for(*function name*)`, where *function name* is the function in `app.py` that you want to route to.

## Independent Lab: Displaying student information

**Important**: Work in the `lab` folder!

### Part 1

In `student.html`, add some text and the templating elements
`{{ student.name }}`, `{{ student.year }}`, and `{{ student.finished_lab }}`.
*Hint*: `student.name` returns the `name` attribute of `student`.

### Part 2

In `app.py`, in the `display_student(student_id)` function, we're going to
use `student_id` to get the student object from the database. Remember that we 
can use `query_by_id(id)`, a function from `database.py` that returns the student
object with the right id.

After getting the right student object from the database, use it as the `student` parameter
to `render_template()`. 

*Hint*: Your code should look something like: `render_template(*filename* id_number=student_id, student=query_by_id(student_id))`.

### Part 3

Refresh your webpage in the browser to make sure everything works as
expected. If there are errors and the server goes down, you can restart
the server from the command line with `python app.py` again.

### Part 4

In `static/style.css` Add your own CSS and additional templating like you've learned in the
past few days!

## Lab Bonus: Listing all students

### Part 1

In `home.html`, add templating code to display the `name`, `year`, and
`finished_lab` status of each student, using `{% for %}` and `{% endfor %}`.


### Part 2

Edit the route to the home page to give `render_template` of `home.html` a list of
students. *Hint*: You'll want to use `query_all()`.

### Part 3

In the `home.html` template, add a link in the same `for` loop which will
bring you to the page for each student.

### Part 4

Again, check that everything works in the browser. Restart your server if
it goes down again, with `python app.py`.


## Additional bonuses

1. Add a new page with all the students from a given year, with a home page
for each year.

2. Figure out a way to add a photo to each student's page.

3. Incorporate a color scheme.
