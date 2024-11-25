# Unit 1

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
