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
