### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  - there are a lot, JavaScript requires the 'let' and 'const' to declare variables, Pthon does not
  - JS requires async and await to make api calls because code does not automaticall stop when a request is sent. python waits for the response
  - JS uses brackets where Python uses indentation to write code blocks


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  - using a try...except can help with this
  - example:
    try:
      val = data['c']
    except: KeyError
      print('cannot find key in data')

- What is a unit test?
  - unit tests test the smaller parts of an application like indivitual functions

- What is an integration test?
  - integrations tests look at the code as a while and find errors in how the application communicates with itself

- What is the role of web application framework, like Flask?
  - frameworks like flask are best used to associate functions and operations with routes in a url. one aprt of an app can make requests to a route with data and that route can perform an operation and give data back to the part of the applicaion that called it

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  - requests like 'foods?type=pretzel' are often used for things like queries where data will be sorted
  - requests like '/foods/pretzel' are better used when there is a part of the application called 'pretzel' that need to be accessed

- How do you collect data from a URL placeholder parameter using Flask?
  - it gets passed into the function that is called with the route handler
  - example:
    @app.route('/foods/<food_name>')
    def get_name_of_foood():
      print(food_name)

- How do you collect data from the query string using Flask?
  - data is collected with request.args
  - example:
    @app.route('/search')
      def search():
      query = request.args.get('q')
      print(query)

- How do you collect data from the body of the request using Flask?
  - by using the request.form call
  - example:
    @app.route('/test', methods=['POST])
    def test():
      name = request.form.get('name')
      email = request.form.get('email')
      print(name, email)

- What is a cookie and what kinds of things are they commonly used for?
  - cookieds are used by a sever to store info about a user in the user's browser

- What is the session object in Flask?
  - session is used to store data similar to cookies, but the storage takes black on the server-side rather than in the user's browser
  - it's used when multiple requests need access to a piece od data for the same user

- What does Flask's `jsonify()` do?
  - it is used to convert Python objects to json so that if a front-end wants json data, python can send it up