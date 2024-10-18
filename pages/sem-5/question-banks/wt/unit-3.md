# Unit 3

## 1) What is AngularJS and what are its main features? How does AngularJS differ from other JavaScript frameworks?

**AngularJS: A Brief Overview and Its Main Features**

AngularJS is an open-source front-end JavaScript framework developed by Google, used for building dynamic, single-page applications. It extends HTML with new attributes and expressions, allowing you to create rich, interactive user interfaces.

**Main Features of AngularJS:**

1. **Two-way Data Binding:** Automatically synchronizes data between model and view, ensuring that changes in one are reflected in the other.
2. **Directives:** Extend HTML with new attributes and elements, enabling you to create reusable, modular components.
3. **Dependency Injection:** Allows for easier testing and maintainability by providing a mechanism to inject dependencies into components.
4. **Templates:** Use plain HTML templates to define the view, with AngularJS expressions to bind data.
5. **Scopes:** Provide a context for expressing dependencies and managing the lifecycle of components.
6. **Routing:** Supports client-side routing, allowing for navigation between views without a full page reload.
7. **Forms:** Offers built-in support for form validation and handling.
8. **Modularity:** Allows you to organize your application into reusable, maintainable modules.
9. **Testing:** Provides built-in support for unit testing and end-to-end testing using tools like Jasmine and Protractor.

**How AngularJS Differs from Other JavaScript Frameworks:**

- **HTML-centric:** AngularJS extends HTML with its own syntax, making it easy to integrate with existing HTML structures and templates.
- **Two-way Data Binding:** Unlike one-way data flow in frameworks like React, AngularJS uses two-way data binding, making it simpler to work with forms and user input.
- **Full-fledged Framework:** AngularJS is a complete framework, providing solutions for routing, forms, and more, while other frameworks like React or Vue focus more on the view layer.
- **Large Community and Support:** AngularJS has a large, active community and is backed by Google, ensuring extensive resources, tutorials, and long-term support.

**Memorable Tip:** Think of AngularJS as a way to supercharge your HTML, making it dynamic and interactive with two-way data binding and reusable components.

**Example of AngularJS Two-way Data Binding:**

```html
<!DOCTYPE html>
<html>
  <script src="<https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular.min.js>"></script>
  <body>
    <div ng-app="myApp" ng-controller="myCtrl">
      <p>First-name: <input type="text" ng-model="firstName" /></p>
      <p>Last-name: <input type="text" ng-model="lastName" /></p>
      <p>Full Name: {{firstName + " " + lastName}}</p>
    </div>

    <script>
      angular.module("myApp", []).controller("myCtrl", function ($scope) {
        $scope.firstName = "John";
        $scope.lastName = "Doe";
      });
    </script>
  </body>
</html>
```

In this example, changes in the input fields are automatically reflected in the full name paragraph, demonstrating AngularJS's two-way data binding.

## 2) What are the core benefits of using AngularJS for web development?

**Core Benefits of Using AngularJS for Web Development:**

1. **Simplified Development:** AngularJS extends HTML with its own syntax, making it easy to create dynamic user interfaces using familiar HTML templates and expressions.
2. **Two-way Data Binding:** Automatically synchronizes data between model and view, reducing boilerplate code and making your application more responsive and intuitive.
3. **Reusability:** With directives, you can create reusable components that can be easily plugged into different parts of your application, promoting code reuse and maintainability.
4. **Efficient Testing:** AngularJS supports dependency injection, making it simpler to write unit tests for your application using tools like Jasmine.
5. **Rich Ecosystem:** Backed by Google, AngularJS has a large, active community, ensuring extensive resources, tutorials, and long-term support. It also integrates well with other tools and services.
6. **Modularity:** Allows you to organize your application into reusable, maintainable modules, making it easier to manage large-scale projects.
7. **Mobile Support:** AngularJS is well-suited for mobile development, with support for single-page applications and touch events. It also integrates with Ionic Framework for building mobile apps.
8. **Performance:** AngularJS uses dirty checking and change detection to efficiently update the DOM, minimizing unnecessary re-renders and improving performance.

**Memorable Tip:** AngularJS makes web development faster, easier, and more maintainable with its simplified development process, two-way data binding, reusability, and efficient testing.

## 3) Explain the MVC (Model-View-Controller) architecture in AngularJS.What are the roles of the Model, View, and Controller in an AngularJS application?

**MVC Architecture in AngularJS:**

AngularJS follows the Model-View-Controller (MVC) architectural pattern, separating an application into three main components: Model, View, and Controller.

**Roles of Model, View, and Controller in AngularJS:**

1. **Model:**

   - Represents the data and the business logic of the application.
   - Acts as an intermediary between the View and the Controller.
   - In AngularJS, the Model is typically an object or a set of objects that contain the data and methods for manipulating that data.
   - Example:

   ```jsx
   angular.module("myApp", []).controller("myCtrl", function ($scope) {
     $scope.user = { name: "John Doe", age: 30 };
   });
   ```

2. **View:**

   - Defines how the data should be presented to the user.
   - In AngularJS, the View is an HTML template that uses AngularJS expressions and directives to bind data from the Model.
   - Example:

   ```html
   <div ng-app="myApp" ng-controller="myCtrl">
     <h1>User Profile</h1>
     <p>Name: {{ user.name }}</p>
     <p>Age: {{ user.age }}</p>
   </div>
   ```

3. **Controller:**

   - Acts as an intermediary between the Model and the View.
   - Contains the logic for updating the Model and the View in response to user input or other events.
   - In AngularJS, the Controller is a JavaScript function that is bound to a specific View using the `ng-controller` directive.
   - Example:

   ```jsx
   angular.module("myApp", []).controller("myCtrl", function ($scope) {
     $scope.user = { name: "John Doe", age: 30 };
     $scope.updateName = function (newName) {
       $scope.user.name = newName;
     };
   });
   ```

**Memorable Tip:** Think of the Model as the data and brains of your application, the View as the face that presents that data, and the Controller as the intermediary that keeps them in sync.

## 4) How does AngularJS implement the MVC pattern in its application structure?

**Implementing MVC in AngularJS Application Structure:**

AngularJS implements the MVC pattern by organizing your application into a specific folder structure and using certain AngularJS features. Here's a simplified, memorable way to understand how AngularJS implements MVC:

1. **Folders and Files:**
   - Create separate folders for `controllers`, `directives`, `filters`, `services`, and `views`.
   - Place related JavaScript files in their respective folders (e.g., `controllers/ userCtrl.js`).
   - Keep your HTML views in the `views` folder (e.g., `views/user.html`).
2. **Module and Controller:**

   - Create an AngularJS module (e.g., `myApp`) that includes the controllers, directives, filters, and services.
   - Controllers act as the glue between the Model and the View. They manage the data and logic for a specific part of your application.
   - Example:

   ```jsx
   // controllers/userCtrl.js
   angular
     .module("myApp")
     .controller("UserCtrl", function ($scope, userService) {
       $scope.user = userService.getUser();
       $scope.updateName = function (newName) {
         userService.updateUser({ name: newName });
       };
     });
   ```

3. **Service as Model:**

   - Services in AngularJS act as the Model, containing the data and business logic for your application.
   - Use services to fetch data, manipulate data, or perform complex operations.
   - Example:

   ```jsx
   // services/userService.js
   angular.module("myApp").service("userService", function () {
     let user = { name: "John Doe", age: 30 };
     this.getUser = function () {
       return user;
     };
     this.updateUser = function (updatedUser) {
       user = angular.extend(user, updatedUser);
     };
   });
   ```

4. **View and Template:**

   - Create HTML templates in the `views` folder that define how the data should be presented.
   - Use AngularJS expressions and directives to bind data from the Controller to the View.
   - Example:

   ```html
   <!-- views/user.html -->
   <div ng-controller="UserCtrl">
     <h1>User Profile</h1>
     <p>Name: <input type="text" ng-model="user.name" /></p>
     <p>Age: {{ user.age }}</p>
   </div>
   ```

**Memorable Tip:** Think of the folder structure as the skeleton of your application, with each folder representing a part of the MVC pattern. Controllers act as the glue between the Model (services) and the View (templates), managing the data and logic for a specific part of your application.

## 5) What are directives in AngularJS, and how do they enhance HTML functionality? Explain the difference between built-in and custom directives in AngularJS.

**Directives in AngularJS:**

Directives in AngularJS are functions that extend the functionality of HTML by adding new attributes, elements, or comments. They enable you to create reusable, modular components and enhance the functionality of your HTML templates.

**How Directives Enhance HTML Functionality:**

1. **Add new attributes:** Directives can add new attributes to HTML elements, allowing you to bind data, listen to events, or perform other tasks.
   - Example: `ng-model`, `ng-click`, `ng-show`
2. **Create new elements:** Directives can create new HTML elements with custom behavior.
   - Example: `ng-app`, `ng-controller`
3. **Replace element content:** Directives can replace the content of an HTML element with custom HTML or dynamic content.
   - Example: `ng-switch`, `ng-include`

**Built-in vs. Custom Directives:**

1. **Built-in Directives:**

   - Provided by AngularJS itself, like `ng-app`, `ng-controller`, `ng-model`, etc.
   - Offer common functionality like data binding, event handling, and conditional rendering.
   - Can be used out-of-the-box without additional configuration.
   - Example:

   ```html
   <div ng-app="myApp" ng-controller="myCtrl">
     <p>Name: <input type="text" ng-model="user.name" /></p>
     <p>Age: {{ user.age }}</p>
   </div>
   ```

2. **Custom Directives:**

   - Created by developers to encapsulate reusable functionality or extend HTML with new behavior.
   - Define a new directive using the `directive` function or the `app.directive` method in an AngularJS module.
   - Can be isolated or shared, with or without a template.
   - Example:

   ```jsx
   angular.module("myApp").directive("userProfile", function () {
     return {
       restrict: "E",
       template: `
         <div>
           <h1>User Profile</h1>
           <p>Name: {{ user.name }}</p>
           <p>Age: {{ user.age }}</p>
         </div>
       `,
       scope: {
         user: "=",
       },
     };
   });
   ```

   ```html
   <div ng-app="myApp" ng-controller="myCtrl">
     <user-profile user="user"></user-profile>
   </div>
   ```

**Memorable Tip:** Think of directives as superpowers for HTML, enabling you to extend its functionality with new attributes, elements, or behavior. Built-in directives offer common functionality, while custom directives allow you to encapsulate reusable code and create unique components.

## 6) Provide examples of common built-in directives in AngularJS.How do you create and use a custom directive in AngularJS?

**Common Built-in Directives in AngularJS:**

1. **ng-app:** Defines the root element of the AngularJS application.
   - Example: `<div ng-app="myApp">`
2. **ng-controller:** Associates an AngularJS controller with an HTML element.
   - Example: `<div ng-controller="myCtrl">`
3. **ng-model:** Binds an HTML form control to an AngularJS model.
   - Example: `<input type="text" ng-model="user.name">`
4. **ng-click:** Binds an event handler to an HTML element's click event.
   - Example: `<button ng-click="updateUser()">Update</button>`
5. **ng-show** and **ng-hide:** Show or hide an HTML element based on an expression's truthiness.
   - Example: `<p ng-show="user.age > 18">You are an adult.</p>`
6. **ng-repeat:** Repeats an HTML element for each item in a collection.
   - Example: `<div ng-repeat="item in items">{{ item }}</div>`
7. **ng-switch:** Conditionally displays one of several HTML elements based on an expression's value.

   - Example:

   ```html
   <div ng-switch="user.role">
     <p ng-switch-when="admin">You are an admin.</p>
     <p ng-switch-when="user">You are a user.</p>
     <p ng-switch-default>You are a guest.</p>
   </div>
   ```

**Creating and Using a Custom Directive in AngularJS:**

1. **Define the directive:**

   - Using the `directive` function:

   ```jsx
   angular.module("myApp").directive("myDirective", function () {
     return {
       restrict: "A",
       template: "<div>This is my custom directive!</div>",
     };
   });
   ```

   - Or using the `app.directive` method:

   ```jsx
   angular.module("myApp").directive("myDirective", function () {
     return {
       restrict: "A",
       template: "<div>This is my custom directive!</div>",
     };
   });
   ```

2. **Use the custom directive in your HTML template:**

   - Add the custom directive as an attribute to an HTML element:

   ```html
   <div my-directive></div>
   ```

   - Or use it as an element (if `restrict: 'E'` is specified):

   ```html
   <my-directive></my-directive>
   ```

**Memorable Tip:** Custom directives in AngularJS allow you to extend HTML functionality and create reusable components. To create a custom directive, define its behavior and template using the `directive` function, and then use it in your HTML templates like any other built-in directive.

## 7) What are expressions in AngularJS, and how are they different from JavaScript expressions? How are AngularJS expressions used in the view (HTML)?

**Expressions in AngularJS:**

AngularJS expressions are similar to JavaScript expressions but have some key differences and additional features. They are used to bind data from the model to the view and perform simple calculations.

**Differences from JavaScript Expressions:**

1. **No Control Flow Statements:** AngularJS expressions cannot contain control flow statements like `if`, `else`, `for`, `while`, etc.
2. **No Function Declarations:** You cannot declare functions within AngularJS expressions.
3. **No Direct DOM Manipulation:** AngularJS expressions cannot directly manipulate the DOM. Instead, they should update the model, which will then be reflected in the view through data binding.
4. **Interpolation Syntax:** AngularJS uses double curly braces (`{{ }}`) for expression interpolation in the view.

**Using AngularJS Expressions in the View (HTML):**

1. **Interpolation:** Binds the value of an expression to an HTML element's content.
   - Example: `<p>{{ user.name }}</p>`
2. **Property Binding:** Binds an expression's value to an HTML element's attribute.
   - Example: `<input type="text" ng-model="user.name">` (uses `ng-model` for two-way data binding)
3. **Event Binding:** Binds an expression to an HTML element's event.
   - Example: `<button ng-click="updateUser()">Update</button>`

**Memorable Tip:** Think of AngularJS expressions as simplified JavaScript expressions that are used to bind data from the model to the view. They have limited functionality compared to JavaScript expressions but are essential for data binding in AngularJS. Use double curly braces (`{{ }}`) for interpolation in your HTML templates to display the value of an expression.

## 8) Discuss how AngularJS expressions are evaluated and how they interact with the scope.

**Evaluating AngularJS Expressions and Interaction with the Scope:**

AngularJS expressions are evaluated in the context of a scope, which acts as the model for the view. Here's how AngularJS expressions are evaluated and interact with the scope:

1. **Scope Association:**
   - Expressions are associated with a specific scope, either the current scope or a child scope.
   - By default, expressions are evaluated in the context of the current scope. However, you can use the `$parent` and `$child` scope properties to access parent or child scopes, respectively.
2. **Expression Parsing and Evaluation:**
   - AngularJS parses the expression and converts it into an Abstract Syntax Tree (AST).
   - The AST is then evaluated in the context of the associated scope, resolving any properties or methods referenced in the expression.
   - Example: In `<p>{{ user.name }}</p>`, AngularJS evaluates `user.name` in the context of the current scope.
3. **Change Detection:**
   - AngularJS uses a change detection mechanism to monitor the model for changes and update the view accordingly.
   - When a model property changes, AngularJS automatically re-evaluates any expressions that depend on that property and updates the view if necessary.
   - Example: If `user.name` changes, AngularJS will update the content of the `<p>{{ user.name }}</p>` element to reflect the new value.
4. **Watchers and Dirty Checking:**
   - AngularJS uses watchers to keep track of changes in the model and trigger view updates.
   - Watchers monitor specific properties on the scope and notify AngularJS when they change.
   - AngularJS uses a process called "dirty checking" to determine which expressions need to be re-evaluated based on the changes in the watched properties.
   - Example: Using `ng-model` adds a watcher for the input element's value, so that changes in the input field update the model and trigger view updates for any expressions that depend on that model property.

**Memorable Tip:** AngularJS expressions are evaluated in the context of a scope, which acts as the model for the view. When a model property changes, AngularJS automatically re-evaluates any expressions that depend on that property and updates the view if necessary. This process is facilitated by watchers and dirty checking, ensuring that the view remains in sync with the model.

## 9) What is the role of a controller in AngularJS? How do you define and use a controller in an AngularJS application?

**Role of a Controller in AngularJS:**

In AngularJS, a controller acts as an intermediary between the model (services) and the view (template). Its primary role is to:

1. **Manage the data:** Fetch data from services, manipulate data, or perform complex operations.
2. **Provide data to the view:** Expose data properties and methods that can be used in the view to display or interact with the data.
3. **Handle user input:** Respond to user events and update the model or view accordingly.

**Defining and Using a Controller in AngularJS:**

1. **Define a Controller:**

   - Using the `controller` function:

   ```jsx
   angular
     .module("myApp")
     .controller("MyController", function ($scope, myService) {
       $scope.user = myService.getUser();
       $scope.updateName = function (newName) {
         myService.updateUser({ name: newName });
       };
     });
   ```

   - Or using the `app.controller` method:

   ```jsx
   angular
     .module("myApp")
     .controller("MyController", function ($scope, myService) {
       // ...
     });
   ```

2. **Inject Dependencies:**
   - Inject services or other dependencies into the controller function using dependency injection.
   - Example: Injecting `myService` into the controller.
3. **Expose Data and Methods:**
   - Define data properties and methods on the `$scope` object that can be used in the view.
   - Example: Exposing `user` and `updateName` on the `$scope` object.
4. **Use the Controller in the View:**
   - Associate the controller with an HTML element using the `ng-controller` directive.
   - Example: `<div ng-controller="MyController">`
   - Access the exposed data and methods in the view using AngularJS expressions.
   - Example: `<p>Name: <input type="text" ng-model="user.name"></p>`

**Memorable Tip:** Think of a controller in AngularJS as the middleman between the model (services) and the view (template). Its role is to manage data, provide data to the view, and handle user input. To define a controller, use the `controller` function or the `app.controller` method, inject dependencies, expose data and methods on the `$scope` object, and then associate the controller with an HTML element using the `ng-controller` directive.

## 10) Explain how controllers interact with views and models in AngularJS.

**Controllers in AngularJS: Interaction with Views and Models**

In AngularJS, controllers interact with views and models to create dynamic, responsive user interfaces. Here's how controllers bridge the gap between views and models:

1. **View to Controller:**

   - The view communicates with the controller using AngularJS directives like `ng-click`, `ng-model`, or custom directives.
   - When a user interacts with the view (e.g., clicks a button, enters text in an input field), the associated directive triggers a function or updates a property on the controller's `$scope` object.
   - Example:

   ```html
   <!-- View -->
   <div ng-controller="MyController">
     <input type="text" ng-model="user.name" />
     <button ng-click="updateUser()">Update</button>
   </div>
   ```

   ```jsx
   // Controller
   angular
     .module("myApp")
     .controller("MyController", function ($scope, myService) {
       $scope.user = myService.getUser();
       $scope.updateUser = function () {
         myService.updateUser($scope.user);
       };
     });
   ```

2. **Controller to Model:**

   - The controller updates the model (services) by calling methods on the injected services.
   - When the controller receives data from the view or needs to fetch data, it interacts with the model to perform the necessary operations.
   - Example:

   ```jsx
   // Controller
   angular
     .module("myApp")
     .controller("MyController", function ($scope, myService) {
       $scope.user = myService.getUser();
       $scope.updateUser = function () {
         myService.updateUser($scope.user).then(function (updatedUser) {
           $scope.user = updatedUser;
         });
       };
     });
   ```

3. **Model to Controller to View:**

   - The model (services) notifies the controller when data changes, either by emitting events or returning promises.
   - The controller listens for these changes and updates the view accordingly by manipulating the `$scope` object.
   - Example:

   ```jsx
   // Controller
   angular
     .module("myApp")
     .controller("MyController", function ($scope, myService) {
       $scope.user = myService.getUser();
       myService.userUpdated.subscribe(function (updatedUser) {
         $scope.user = updatedUser;
       });
     });
   ```

**Memorable Tip:** Controllers in AngularJS act as a bridge between views and models. They receive input from the view, update the model, and then update the view with the latest data. This process ensures that the view remains in sync with the model, creating a responsive and dynamic user interface.

## 11) What are filters in AngularJS and how are they used to format data? How do you create and apply a custom filter in AngularJS?

**Filters in AngularJS: Data Formatting and Customization**

Filters in AngularJS are used to format data and transform it into a more readable or usable format. They can be applied to expressions in the view or used in controllers to manipulate data.

**Using Built-in Filters:**

1. **Currency:** Formats a number as currency.
   - Example: `{{ price | currency }}`
2. **Date:** Formats a date as a string.
   - Example: `{{ date | date }}`
3. **LimitTo:** Limits the number of elements in an array.
   - Example: `{{ [1,2,3,4,5] | limitTo:3 }}`
4. **OrderBy:** Sorts an array of objects by a specific property.
   - Example: `{{ users | orderBy:'lastName' }}`

**Creating a Custom Filter:**

1. **Define the Filter:**

   - Using the `filter` function:

   ```jsx
   angular.module("myApp").filter("reverse", function () {
     return function (input) {
       return input.split("").reverse().join("");
     };
   });
   ```

   - Or using the `app.filter` method:

   ```jsx
   angular.module("myApp").filter("reverse", function () {
     return function (input) {
       return input.split("").reverse().join("");
     };
   });
   ```

2. **Apply the Custom Filter:**
   - In the view, using the pipe (`|`) syntax:
   - Example: `{{ text | reverse }}`
   - In a controller, by calling the filter function:
   - Example: `var reversedText = reverseFilter(text);`

**Memorable Tip:** Filters in AngularJS help format data for better readability and usability. You can use built-in filters or create custom filters to transform data as needed. To create a custom filter, define a function that takes input and returns the transformed output, then apply it in the view or controller using the pipe (`|`) syntax or by calling the filter function directly.

## 12) Discuss the built-in filters available in AngularJS. Provide examples of their usage.

**Built-in Filters in AngularJS: Data Transformation Made Easy**

AngularJS offers several built-in filters to help you transform and format data in your views. Here are some commonly used built-in filters with examples of their usage:

1. **currency:** Formats a number as currency with a specified currency symbol and decimal places.
   - Usage: `{{ price | currency:'$':2 }}` → `$1,234.56`
   - Example: `<p>Price: {{ price | currency:'$':2 }}</p>`
2. **date:** Formats a date as a string with a specified format.
   - Usage: `{{ date | date:'MM/dd/yyyy' }}` → `04/15/2022`
   - Example: `<p>Birthdate: {{ user.birthdate | date:'MM/dd/yyyy' }}</p>`
3. **filter:** Filters an array of objects based on a search term and a property.

   - Usage: `{{ users | filter:searchTerm:'name' }}`
   - Example:

   ```html
   <input type="text" ng-model="searchTerm" />
   <ul>
     <li ng-repeat="user in users | filter:searchTerm:'name'">
       {{ user.name }}
     </li>
   </ul>
   ```

4. **limitTo:** Limits the number of elements in an array.
   - Usage: `{{ [1,2,3,4,5] | limitTo:3 }}` → `[1,2,3]`
   - Example: `<ul><li ng-repeat="item in [1,2,3,4,5] | limitTo:3">{{ item }}</li></ul>`
5. **lowercase** and **uppercase:** Converts a string to lowercase or uppercase, respectively.
   - Usage: `{{ text | lowercase }}` → `hello world`
   - Example: `<p>Enter text: <input type="text" ng-model="text"><br>Lowercase: {{ text | lowercase }}</p>`
6. **orderBy:** Sorts an array of objects by a specific property or properties.

   - Usage: `{{ users | orderBy:'lastName' }}` or `{{ users | orderBy:'-lastName' }}` (for descending order)
   - Example:

   ```html
   <table>
     <tr>
       <th>Name</th>
       <th>Last Name</th>
     </tr>
     <tr ng-repeat="user in users | orderBy:'lastName'">
       <td>{{ user.firstName }}</td>
       <td>{{ user.lastName }}</td>
     </tr>
   </table>
   ```

**Memorable Tip:** AngularJS's built-in filters help you transform and format data quickly and easily. Use them to display currency, dates, filtered arrays, limited arrays, case-converted strings, and sorted arrays in your views.

## 13) What are modules in AngularJS, and what is their purpose?

**Modules in AngularJS: Organizing and Structuring Your Application**

In AngularJS, modules are used to organize and structure your application by grouping related functionality together. They serve as containers for controllers, directives, filters, and services, allowing you to maintain a clear and modular codebase.

**Purpose of Modules in AngularJS:**

1. **Dependency Management:** Modules allow you to manage dependencies between components, ensuring that each part of your application has access to the required services, controllers, directives, and filters.
2. **Code Organization:** By grouping related functionality together, modules help keep your codebase organized and maintainable. They enable you to work on specific parts of your application in isolation.
3. **Reusability:** Modules can be shared between applications, promoting code reuse and reducing duplication. You can also create reusable, modular components that can be easily plugged into different projects.
4. **Configuration and Initialization:** Modules provide a place to configure and initialize your application, allowing you to set up routing, run bootstrapping code, and define application-wide settings.

**Creating and Using Modules in AngularJS:**

1. **Create a Module:**

   - Using the `angular.module` function:

   ```jsx
   var myApp = angular.module("myApp", []);
   ```

   - Or using the `app` service:

   ```jsx
   var myApp = angular.module("myApp", []);
   ```

2. **Add Dependencies:**
   - Pass an array of dependencies to the `angular.module` function to create a new module with access to those dependencies.
   - Example: `var myApp = angular.module('myApp', ['ngRoute', 'myServices']);`
3. **Register Components:**

   - Register controllers, directives, filters, and services with the module using the appropriate methods (e.g., `controller`, `directive`, `filter`, `service`).
   - Example:

   ```jsx
   myApp.controller("MyController", function ($scope) {
     // ...
   });

   myApp.directive("myDirective", function () {
     // ...
   });

   myApp.filter("myFilter", function () {
     // ...
   });

   myApp.service("myService", function () {
     // ...
   });
   ```

**Memorable Tip:** Modules in AngularJS are essential for organizing and structuring your application. They help manage dependencies, promote code reuse, and simplify configuration and initialization. Create modules using the `angular.module` function, add dependencies, and register components like controllers, directives, filters, and services to keep your codebase organized and maintainable.

## 14) How do you create and configure a module in AngularJS? Explain the role of modules in organising and managing AngularJS applications.

**Creating and Configuring Modules in AngularJS:**

1. **Create a Module:**

   - Using the `angular.module` function:

   ```jsx
   var myApp = angular.module("myApp", []);
   ```

2. **Add Dependencies:**
   - Pass an array of dependencies to create a new module with access to those dependencies.
   - Example: `var myApp = angular.module('myApp', ['ngRoute', 'myServices']);`
3. **Register Components:**

   - Add controllers, directives, filters, and services to the module using the appropriate methods.
   - Example:

   ```jsx
   myApp.controller("MyController", function ($scope) {
     // ...
   });

   myApp.directive("myDirective", function () {
     // ...
   });

   myApp.filter("myFilter", function () {
     // ...
   });

   myApp.service("myService", function () {
     // ...
   });
   ```

**Role of Modules in Organizing AngularJS Applications:**

Modules help manage and structure your AngularJS application by:

1. **Grouping Related Functionality:** Modules keep related controllers, directives, filters, and services together, making your codebase easier to understand and maintain.
2. **Managing Dependencies:** Modules allow you to specify dependencies between components, ensuring that each part of your application has access to the required services and other modules.
3. **Promoting Code Reuse:** By encapsulating functionality within modules, you can easily share and reuse them across different applications or projects.
4. **Simplifying Configuration:** Modules provide a central place to configure and initialize your application, making it easier to set up routing, run bootstrapping code, and define application-wide settings.

**Memorable Tip:** Modules in AngularJS are like boxes that hold related components together. They help keep your code organized, manage dependencies, promote code reuse, and simplify configuration. Create modules using the `angular.module` function, add dependencies, and register components to maintain a well-structured and manageable AngularJS application.

## 15) How does AngularJS handle forms and form validation? How can you implement form validation in AngularJS? Provide examples of built-in validation directives.

**AngularJS Form Handling and Validation:**

AngularJS simplifies form handling and validation by using data binding and built-in directives. It supports two-way data binding, which means that changes in the model are reflected in the view, and vice versa.

**Built-in Validation Directives:**

1. **ng-model:** Binds form controls to the model. It also provides basic validation by updating the model when the input changes.

   - Example:

   ```html
   <input type="text" ng-model="user.name" />
   ```

2. **ng-required:** Marks a form control as required. If the control is empty, AngularJS will add a validation error.

   - Example:

   ```html
   <input type="text" ng-model="user.name" ng-required="true" />
   ```

3. **ng-minlength** and **ng-maxlength:** Set minimum and maximum length for input fields.

   - Example:

   ```html
   <input type="text" ng-model="user.name" ng-minlength="3" ng-maxlength="20" />
   ```

4. **ng-pattern:** Validates input against a regular expression pattern.

   - Example:

   ```html
   <input
     type="text"
     ng-model="user.email"
     ng-pattern="/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/"
   />
   ```

**Form Validation with ng-form and ng-invalid:**

1. **ng-form:** Groups form controls and enables form-level validation.

   - Example:

   ```html
   <form ng-form="userForm">
     <input type="text" ng-model="user.name" ng-required="true" />
     <input
       type="email"
       ng-model="user.email"
       ng-required="true"
       ng-pattern="/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/"
     />
     <button type="submit" ng-disabled="userForm.$invalid">Submit</button>
   </form>
   ```

2. **ng-invalid:** Marks a form control as invalid when a validation error occurs.

   - Example:

   ```html
   <input
     type="text"
     ng-model="user.name"
     ng-required="true"
     ng-invalid="userForm.name.$invalid"
   />
   ```

**Memorable Tip:** AngularJS makes form handling and validation easy with built-in directives like `ng-model`, `ng-required`, `ng-minlength`, `ng-maxlength`, and `ng-pattern`. Use `ng-form` to group form controls and enable form-level validation. The `ng-invalid` directive marks form controls as invalid when validation errors occur.

## 16) What is the scope in AngularJS and how does it function?

**Scope in AngularJS:**

In AngularJS, the scope is an object that ties the model to the view. It acts as a bridge between the controller and the view, providing a place to store data and functions that can be accessed and manipulated in the view.

**How Scope Functions in AngularJS:**

1. **Prototype Inheritance:** Scopes in AngularJS use prototype inheritance to create a hierarchical structure. Each scope has access to properties and methods defined on its parent scope through prototype inheritance.

   - Example:

   ```jsx
   $scope.user = { name: "John Doe" };
   $scope.userProfile = function () {
     return "Profile of " + $scope.user.name;
   };
   ```

   ```html
   <div ng-controller="MyController">
     <p>Name: {{ user.name }}</p>
     <p>Profile: {{ userProfile() }}</p>
     <div ng-controller="ChildController">
       <p>Profile: {{ userProfile() }}</p>
       <!-- Accesses the same user and userProfile from the parent scope -->
     </div>
   </div>
   ```

2. **Isolation:** Child scopes are isolated from their parent scopes, meaning that changes to properties on a child scope do not affect the parent scope.

   - Example:

   ```jsx
   $scope.user = { name: "John Doe" };
   $scope.$new().user = { name: "Jane Doe" }; // Creates a new, isolated scope with its own user property
   ```

3. **Watchers and Digests:** Scopes use watchers to monitor changes in the model and trigger view updates. The digest cycle is responsible for checking if any watched expressions have changed and updating the view accordingly.

   - Example:

   ```jsx
   $scope.$watch("user.name", function (newValue, oldValue) {
     if (newValue !== oldValue) {
       console.log("User name changed from", oldValue, "to", newValue);
     }
   });
   ```

**Memorable Tip:** The scope in AngularJS is an object that connects the model to the view. It uses prototype inheritance to create a hierarchical structure, allowing child scopes to access properties and methods from their parent scopes. Scopes are isolated from one another, ensuring that changes to one scope do not affect others. The scope uses watchers and the digest cycle to monitor changes in the model and update the view accordingly.

## 17) Explain the relationship between the scope and the model in AngularJS.

**Scope and Model Relationship in AngularJS:**

In AngularJS, the scope and the model have a tight, bi-directional relationship. The model is the data that the view displays and interacts with, while the scope is the object that ties the model to the view. Here's how they relate to each other:

1. **Model as Scope Properties:** The model is represented as properties on the scope. The controller populates these properties with data, and the view displays and manipulates them.

   - Example:

   ```jsx
   // Controller
   angular.module("myApp").controller("MyController", function ($scope) {
     $scope.user = { name: "John Doe", age: 30 };
   });
   ```

   ```html
   <!-- View -->
   <div ng-controller="MyController">
     <p>Name: {{ user.name }}</p>
     <p>Age: {{ user.age }}</p>
   </div>
   ```

2. **Two-Way Data Binding:** AngularJS uses two-way data binding to keep the model and the view in sync. Changes in the model are reflected in the view, and changes in the view are reflected in the model.

   - Example:

   ```html
   <!-- View -->
   <div ng-controller="MyController">
     <input type="text" ng-model="user.name" />
     <p>You entered: {{ user.name }}</p>
   </div>
   ```

   In this example, typing in the input field updates the `user.name` model property, and the paragraph displays the current value of `user.name`.
