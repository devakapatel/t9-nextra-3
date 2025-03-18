# Assignment 3

## 1) What is AngularJS and what are its main features? How does AngularJS differ from other JavaScript frameworks?

**AngularJS: A Powerful JavaScript Framework**

AngularJS, often referred to as Angular 1, is an open-source JavaScript framework developed by Google. It's used for building dynamic web applications. Here are its main features:

1. **Two-Way Data Binding**: This means changes in the model are reflected in the view, and vice versa, automatically. It simplifies the development process significantly.

2. **Dependency Injection**: This is a design pattern that allows for better code organization, testability, and maintainability.

3. **Directives**: These are extensions to HTML that allow you to create reusable components. They help in creating custom HTML tags and attributes.

4. **Scopes**: Scopes are JavaScript objects that refer to the model. They help manage the data flow between the view and the controller.

5. **Templates**: AngularJS uses HTML templates to define the view. It's easy to understand and write, as it's similar to regular HTML.

**AngularJS vs Other JavaScript Frameworks**

AngularJS differs from other JavaScript frameworks like React, Vue, or jQuery in several ways:

- **Structure and Organization**: AngularJS encourages a structured, component-based approach to building applications. Other frameworks like React or Vue also use components, but AngularJS has a more opinionated structure.

- **Two-Way Data Binding**: While some frameworks like Vue also offer two-way data binding, it's a core feature of AngularJS. In React, you manage data flow manually.

- **Dependency Injection**: This is a unique feature of AngularJS that promotes code modularity and testability. Other frameworks don't have this built-in.

- **Learning Curve**: AngularJS has a steeper learning curve compared to some other frameworks. It has its own way of doing things, which can be both a strength and a weakness.

- **Community and Support**: AngularJS has a large community and is backed by Google, which means you'll find plenty of resources and support online. However, it's not as popular as it once was, with Angular (Angular 2 and later) being the current focus of Google.

## 2) Explain the MVC (Model-View-Controller) architecture in AngularJS.What are the roles of the Model, View, and Controller in an AngularJS application?

**AngularJS's MVC Architecture: A Simple Explanation**

AngularJS follows the Model-View-Controller (MVC) architectural pattern, which helps separate concerns and makes your code more manageable. Here's a simple breakdown:

1. **Model**: This is the data layer of your application. In AngularJS, the model is typically a JavaScript object that holds data. It's responsible for:

   - Storing and managing data.
   - Providing methods to manipulate this data.

2. **View**: This is the presentation layer, or the user interface. In AngularJS, views are defined using HTML templates. They are responsible for:

   - Displaying the data from the model.
   - Handling user interactions and updating the model.

3. **Controller**: This acts as a bridge between the model and the view. In AngularJS, controllers are JavaScript functions that are bound to a specific view. They are responsible for:
   - Managing the flow of data between the model and the view.
   - Containing the business logic of your application.

**How They Work Together**

- The controller watches for changes in the model and updates the view accordingly. This is done using AngularJS's two-way data binding.
- The view listens for changes in the controller and updates itself to reflect those changes.
- The controller also handles user interactions, updating the model when necessary, and then the view is updated automatically.

**A Simple Example**

Here's a simple example:

- **Model**: A JavaScript object `{name: 'John', age: 30}`
- **Controller**: A function that watches this object and updates a view when it changes.
- **View**: An HTML template that displays the name and age, and has a button to update the age.

In this example, when the age is updated in the controller, the view updates automatically to reflect this change. This is the essence of AngularJS's MVC pattern.

## 3) What are directives in AngularJS, and how do they enhance HTML functionality? Explain the difference between built-in and custom directives in AngularJS.

**Directives: Supercharging HTML in AngularJS**

In AngularJS, directives are like special powers for HTML. They extend the functionality of HTML by letting you create new HTML tags and attributes. Here's how they work:

- **Purpose**: Directives tell AngularJS to attach a special behavior to an HTML tag or attribute.
- **Syntax**: They start with `ng-` (like `ng-model`, `ng-repeat`) or are custom elements (like `<my-directive>`).
- **Example**: `<input type="text" ng-model="user.name">` - Here, `ng-model` is a directive that binds the input field to the `user.name` model.

**Built-in vs Custom Directives**

- **Built-in Directives**: These are provided by AngularJS itself, like `ng-model`, `ng-repeat`, `ng-if`, etc. They handle common tasks like data binding, looping, and conditional rendering. You can use them out-of-the-box.

  - _Example_: `<div ng-if="show">This will only show if show is true.</div>`

- **Custom Directives**: These are directives you create yourself to add specific functionality to your app. They start with a prefix (like `app-`) to avoid conflicts with built-in directives.
  - _Example_: `<app-highlight color="red">This text will be red.</app-highlight>`

**How Custom Directives Work**

Custom directives are defined using the `directive` function in AngularJS. Here's a simple example:

```javascript
app.directive("appHighlight", function () {
  return {
    restrict: "E", // This makes it an element directive (like <app-highlight>)
    scope: { color: "=" }, // This binds the color attribute to the directive's scope
    template: '<span ng-bind="color" style="color: {{color}};">{{text}}</span>', // This is the HTML template for the directive
  };
});
```

In this example, `appHighlight` is a custom directive that creates a span with the text color set to the value of the `color` attribute.

## 4) What are expressions in AngularJS, and how are they different from JavaScript expressions? How are AngularJS expressions used in the view (HTML)?

**AngularJS Expressions: A Brief Overview**

In AngularJS, expressions are a key part of data binding. They allow you to display and manipulate model data in your views. Here's how they differ from regular JavaScript expressions and how they're used in the view:

**Differences from JavaScript Expressions**

- **Purpose**: JavaScript expressions are used for calculations and comparisons. AngularJS expressions, on the other hand, are used to display and manipulate data in your views.
- **Syntax**: JavaScript expressions can be complex, with multiple operators and functions. AngularJS expressions are simpler and more limited in scope. They can only access data from the current scope and have limited operators (like `+`, `-`, `*`, `/`, `%`, `===`, `!==`, `==`, `!=`, `&&`, `||`, `? :`).
- **Evaluation**: JavaScript expressions are evaluated immediately when the script runs. AngularJS expressions are evaluated whenever the data they're bound to changes, thanks to AngularJS's two-way data binding.

**Using AngularJS Expressions in the View**

AngularJS expressions are used in your HTML templates to display model data and perform simple calculations. Here's how:

- **Interpolation**: This is the most common way to use expressions. It's done using double curly braces `{{ }}`. For example:

  ```html
  <p>Hello, {{user.name}}!</p>
  ```

  In this case, `{{user.name}}` is an expression that displays the value of `user.name` from the current scope.

- **Attribute Binding**: Expressions can also be used to bind attributes to model data. For example:

  ```html
  <input type="text" ng-model="user.name" />
  ```

  Here, `ng-model` is a directive that binds the input field to the `user.name` model. The expression `user.name` sets the initial value of the input field.

- **ng-repeat**: This directive uses expressions to loop over an array. For example:
  ```html
  <div ng-repeat="item in items">{{item.name}}</div>
  ```
  Here, `item in items` is an expression that loops over the `items` array, and `{{item.name}}` displays the name of the current item.

## 5) What is the role of a controller in AngularJS? How do you define and use a controller in an AngularJS application?

**AngularJS Expressions: A Brief Overview**

In AngularJS, expressions are a key part of data binding. They allow you to display and manipulate model data in your views. Here's how they differ from regular JavaScript expressions and how they're used in the view:

**Differences from JavaScript Expressions**

- **Purpose**: JavaScript expressions are used for calculations and comparisons. AngularJS expressions, on the other hand, are used to display and manipulate data in your views.
- **Syntax**: JavaScript expressions can be complex, with multiple operators and functions. AngularJS expressions are simpler and more limited in scope. They can only access data from the current scope and have limited operators (like `+`, `-`, `*`, `/`, `%`, `===`, `!==`, `==`, `!=`, `&&`, `||`, `? :`).
- **Evaluation**: JavaScript expressions are evaluated immediately when the script runs. AngularJS expressions are evaluated whenever the data they're bound to changes, thanks to AngularJS's two-way data binding.

**Using AngularJS Expressions in the View**

AngularJS expressions are used in your HTML templates to display model data and perform simple calculations. Here's how:

- **Interpolation**: This is the most common way to use expressions. It's done using double curly braces `{{ }}`. For example:

  ```html
  <p>Hello, {{user.name}}!</p>
  ```

  In this case, `{{user.name}}` is an expression that displays the value of `user.name` from the current scope.

- **Attribute Binding**: Expressions can also be used to bind attributes to model data. For example:

  ```html
  <input type="text" ng-model="user.name" />
  ```

  Here, `ng-model` is a directive that binds the input field to the `user.name` model. The expression `user.name` sets the initial value of the input field.

- **ng-repeat**: This directive uses expressions to loop over an array. For example:
  ```html
  <div ng-repeat="item in items">{{item.name}}</div>
  ```
  Here, `item in items` is an expression that loops over the `items` array, and `{{item.name}}` displays the name of the current item.

## 6) What are filters in AngularJS and how are they used to format data? How do you create and apply a custom filter in AngularJS?

**AngularJS Filters: Transforming Data for Display**

Filters in AngularJS are used to format and transform data before it's displayed in the view. They help make data more readable and usable. Here's how they work and how to create a custom one:

**Built-in Filters**

AngularJS provides several built-in filters like `currency`, `date`, `uppercase`, `lowercase`, etc. They're used in expressions like this:

```html
<p>Price: {{price | currency}}</p>
<p>Date: {{date | date: 'full'}}</p>
<p>Name: {{name | uppercase}}</p>
```

**Creating a Custom Filter**

To create a custom filter, you use the `filter` function in AngularJS. Here's a simple example of a filter that adds a greeting to a name:

```javascript
app.filter("greeting", function () {
  return function (input) {
    if (input) {
      return "Hello, " + input;
    } else {
      return "";
    }
  };
});
```

In this example, `greeting` is the name of the filter. The function it returns takes an input, adds a greeting, and returns the result.

**Applying a Custom Filter**

To use this custom filter in your view, you simply include it in your expression:

```html
<p>Greeting: {{name | greeting}}</p>
```

**Filter Arguments**

Filters can also take arguments. To pass an argument, you separate it from the filter name with a colon:

```javascript
app.filter("greeting", function () {
  return function (input, greeting) {
    if (input) {
      return greeting + ", " + input;
    } else {
      return "";
    }
  };
});
```

Now, you can use the filter like this:

```html
<p>Greeting: {{name | greeting:'Hi'}}</p>
```

In this case, the filter will add "Hi, " instead of "Hello, " to the name.

## 7) What are modules in AngularJS, and what is their purpose? How do you create and configure a module in AngularJS? Explain the role of modules in organizing and managing AngularJS applications.

**AngularJS Modules: Organizing and Managing Applications**

In AngularJS, modules are the fundamental building blocks of an application. They help organize and manage your code, making it more modular, scalable, and maintainable. Here's what modules are, their purpose, and how to create and configure them:

**Purpose of Modules**

- **Code Organization**: Modules help group related functionality together, making your codebase easier to understand and navigate.
- **Dependency Management**: Modules allow you to declare dependencies, ensuring that your code has access to the necessary functionality.
- **Isolation**: Modules help isolate code from each other, reducing the chances of conflicts and making your application more robust.

**Creating and Configuring a Module**

To create a module in AngularJS, you use the `angular.module` function. Here's a basic example:

```javascript
// Create a module named 'myApp'
var myApp = angular.module("myApp", []);

// Add a controller to the module
myApp.controller("MyController", function ($scope) {
  $scope.message = "Hello, World!";
});
```

In this example, `myApp` is a module with no dependencies (the second argument is an empty array). We then add a controller to this module using the `.controller` method.

**Configuring Modules**

Modules can also be configured using configuration blocks. Here's an example of configuring a module to use a service:

```javascript
// Create a service
myApp.service("myService", function () {
  this.getMessage = function () {
    return "Hello, World!";
  };
});

// Configure the module to use the service
myApp.controller("MyController", [
  "myService",
  function (myService, $scope) {
    $scope.message = myService.getMessage();
  },
]);
```

In this example, we first create a service `myService`. Then, we configure the `MyController` to use this service by injecting it as a dependency. The `'myService'` string is the name of the service, and `function(myService, $scope)` is the controller function that takes the service as an argument.

**The Role of Modules in Organizing Applications**

Modules play a crucial role in organizing and managing AngularJS applications by:

- **Dividing the Application into Smaller Parts**: Each module can contain related functionality, making the application easier to understand and maintain.

- **Managing Dependencies**: Modules allow you to declare dependencies, ensuring that your code has access to the necessary functionality. This helps prevent conflicts and makes your code more robust.

- **Isolating Code**: Modules help isolate code from each other, reducing the chances of conflicts and making your application more robust.

- **Facilitating Reusability**: Modules can be reused in other applications, promoting code reuse and reducing duplication.

In summary, modules are a key feature of AngularJS that help organize and manage your code, making your applications more modular, scalable, and maintainable.

## 8) How does AngularJS handle forms and form validation? How can you implement form validation in AngularJS? Provide examples of built-in validation directives.

**AngularJS Forms and Form Validation: A Simple Guide**

AngularJS provides built-in support for forms and form validation, making it easy to handle user input and ensure data quality. Here's how it works and how to implement form validation:

**Handling Forms**

AngularJS uses the `ng-form` directive to create forms. It also provides the `ng-model` directive to bind form controls to model data. Here's a simple example:

```html
<form ng-form="userForm">
  <input type="text" ng-model="user.name" />
  <input type="email" ng-model="user.email" />
  <button ng-disabled="userForm.$invalid">Submit</button>
</form>
```

In this example, `ng-form` creates a form named `userForm`, and `ng-model` binds the form controls to the `user` model. The `ng-disabled` directive disables the submit button when the form is invalid.

**Form Validation**

AngularJS provides built-in validation directives to validate form input. Here are some examples:

1. **Required**: The `ng-required` directive marks a field as required. If the field is empty, the form will be invalid.

   ```html
   <input type="text" ng-model="user.name" ng-required="true" />
   ```

2. **Email**: The `ng-pattern` directive with the email pattern (`/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/`) validates that the input is an email address.

   ```html
   <input
     type="text"
     ng-model="user.email"
     ng-pattern="/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/"
   />
   ```

3. **Minlength and Maxlength**: The `ng-minlength` and `ng-maxlength` directives validate the length of the input.

   ```html
   <input type="text" ng-model="user.name" ng-minlength="3" ng-maxlength="20" />
   ```

4. **Number**: The `ng-pattern` directive with the number pattern (`/^\d+$/`) validates that the input is a number.

   ```html
   <input type="text" ng-model="user.age" ng-pattern="/^\d+$/" />
   ```

**Custom Validation**

You can also create custom validation using the `$validators` property of the form controller. Here's an example of a custom validation that checks if a password is strong:

```javascript
app.directive("strongPassword", function () {
  return {
    require: "ngModel",
    link: function (scope, elem, attrs, ctrl) {
      ctrl.$validators.strongPassword = function (modelValue, viewValue) {
        if (ctrl.$isEmpty(viewValue)) {
          return true;
        }
        var re = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;
        return re.test(viewValue);
      };
    },
  };
});
```

In this example, the `strongPassword` directive adds a custom validation to the `ngModel` controller. The validation checks if the password is at least 8 characters long and contains at least one lowercase letter, one uppercase letter, and one number.

**Displaying Validation Errors**

To display validation errors, you can use the `$error` property of the form controller. Here's an example:

```html
<form ng-form="userForm">
  <input type="text" ng-model="user.name" ng-required="true" />
  <div ng-show="userForm.name.$error.required">Name is required</div>
  <input
    type="email"
    ng-model="user.email"
    ng-pattern="/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/"
  />
  <div ng-show="userForm.email.$error.pattern">
    Please enter a valid email address
  </div>
  <button ng-disabled="userForm.$invalid">Submit</button>
</form>
```

In this example, the validation error messages are displayed when the corresponding validation error is present in the `$error` property of the form controller.

## 9) What is the scope in AngularJS and how does it function?What are services in AngularJS, and why are they used? How do you create and use a service in AngularJS?

**Scope in AngularJS: A Crucial Part of the MVC Architecture**

In AngularJS, scope is a key part of the Model-View-Controller (MVC) architecture. It acts as a bridge between the model and the view, providing a context for data and functions that can be accessed by the view.

**What is Scope?**

Scope is an object that refers to the application model. It holds data that can be accessed and manipulated by the view, and it provides functions that can be called by the view.

**How Does Scope Function?**

- **Data Binding**: Scope provides data binding, which means it automatically synchronizes the data between the model and the view. When the data in the scope changes, the view updates automatically, and vice versa.

- **Event Handling**: Scope allows the view to listen for and respond to events. For example, when a user clicks a button, the scope can trigger a function to update the model.

- **Function Calling**: Scope provides functions that can be called by the view to manipulate the model.

**Services in AngularJS: Facilitating Code Reuse and Separation of Concerns**

Services in AngularJS are used to organize and share code across your application. They help separate concerns, promote code reuse, and make your application more modular and maintainable.

**What are Services?**

Services are singleton objects that hold and provide functionality. They can be injected into controllers, directives, and other services, allowing you to share code and data across your application.

**Why are Services Used?**

- **Code Reuse**: Services allow you to write code once and reuse it in multiple places.

- **Separation of Concerns**: Services help separate concerns by encapsulating functionality that can be used across the application.

- **Testability**: Services can be tested in isolation, making your application easier to test.

**Creating and Using a Service in AngularJS**

Here's how to create and use a service in AngularJS:

**Creating a Service**

```javascript
// Create a service named 'myService'
app.service("myService", function () {
  this.getMessage = function () {
    return "Hello, World!";
  };
});
```

In this example, `myService` is a service that provides a `getMessage` function.

**Using a Service**

To use a service, you inject it into the object where you want to use it. Here's how to use `myService` in a controller:

```javascript
// Inject myService into the controller
app.controller("MyController", [
  "myService",
  function (myService, $scope) {
    $scope.message = myService.getMessage();
  },
]);
```

In this example, `myService` is injected into the `MyController` as a dependency. The controller then uses the `getMessage` function to set the value of `$scope.message`.

**Using Services in Views**

To use a service in a view, you can access it through the controller's scope:

```html
<p>{{message}}</p>
```

In this example, the view displays the value of `$scope.message`, which was set using the `myService` service in the controller.

**Injecting Services into Directives**

Services can also be injected into directives to provide functionality:

```javascript
app.directive("myDirective", [
  "myService",
  function (myService) {
    return {
      link: function (scope, elem, attrs) {
        elem.text(myService.getMessage());
      },
    };
  },
]);
```

In this example, `myDirective` is a directive that uses the `myService` service to set the text of the element it's bound to.

## 10) Write Short Notes on: (a) AJAX (b) DOM

**(a) AJAX**

- **Asynchronous JavaScript and XML**
- Enables web pages to update asynchronously by exchanging data with a web server behind the scenes.
- Allows web applications to send and receive data from a server without interfering with the display and behavior of the existing page.
- Key features:
  - Asynchronous: Updates occur in the background without refreshing the page.
  - Data exchange: Uses HTTP methods (GET, POST, PUT, DELETE) to send and receive data.
  - Lightweight: Only updates the necessary parts of the page, reducing data transfer and improving performance.
- Used in: Single-page applications (SPAs), improving user experience by providing real-time updates and reducing page reloads.

**(b) DOM**

- **Document Object Model**
- A programming interface for web documents, providing a structured representation of the document as a tree-like model.
- The DOM represents the document as nodes and objects, allowing programming languages (like JavaScript) to manipulate the document, its style, and content.
- Key features:
  - Tree-like structure: Documents are represented as a hierarchical tree of nodes.
  - Node types: Includes elements, attributes, text, comments, and more.
  - Manipulation: Allows adding, removing, and modifying elements and attributes.
- Used in: Web development to dynamically update and interact with web pages, create responsive designs, and handle user events.
