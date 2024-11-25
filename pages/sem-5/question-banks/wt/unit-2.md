# Unit 2

## 1) What is CSS? Describe the different ways to apply CSS to an HTML document.

**CSS (Cascading Style Sheets):**

- A style sheet language used to describe the look and formatting of a document written in HTML or XML.
- Separates presentation (CSS) from content (HTML), improving accessibility and maintainability.

**Ways to apply CSS to an HTML document:**

1. **Inline CSS**: Applied directly to an HTML element using the `style` attribute.
   - Example: `<p style="color: blue;">This is an inline CSS example.</p>`
2. **Internal CSS**: Defined within a `<style>` block in the `<head>` section of an HTML document.

   - Example:

   ```html
   <head>
     <style>
       p {
         color: blue;
       }
     </style>
   </head>
   ```

3. **External CSS**: Defined in a separate .css file, linked to the HTML document using the `<link>` element in the `<head>` section.

   - Example:

   ```html
   <head>
     <link rel="stylesheet" href="styles.css" />
   </head>
   ```

   - `styles.css`:

   ```css
   p {
     color: blue;
   }
   ```

4. **Imported CSS**: Importing one external style sheet into another using the `@import` rule.

   - Example:

   ```css
   @import url("styles1.css");
   @import url("styles2.css");
   ```

## 2) What are the key differences between inline, internal, and external CSS?

- **Inline CSS**:
  - Applied directly to an HTML element using `style` attribute.
  - High specificity, takes precedence over other CSS rules.
  - Not reusable, applies only to the specific element.
- **Internal CSS**:
  - Defined within `<style>` block in the `<head>` section of an HTML document.
  - Reusable within the same document, but not across multiple documents.
  - Specificity depends on selector usage.
- **External CSS**:
  - Defined in a separate .css file, linked to HTML using `<link>` in `<head>`.
  - Highly reusable, can be used across multiple documents.
  - Specificity depends on selector usage, but generally lower than inline or internal CSS due to being applied globally.

## 3) Explain the CSS box model and its components.

### The CSS Box Model

The CSS box model is a fundamental concept in web design and development that describes how elements on a web page are structured and how their dimensions are calculated. Every HTML element is considered a rectangular box, and the box model defines the space around these boxes, including their content, padding, borders, and margins.

#### Components of the CSS Box Model

The box model consists of the following components:

#### 1. **Content**

- **Description**: This is the innermost part of the box where text, images, or other media are displayed.
- **Properties**: The size of the content area can be controlled using properties like `width` and `height`.

#### Example:

```css
.box {
  width: 200px; /* Width of the content area */
  height: 100px; /* Height of the content area */
}
```

#### 2. **Padding**

- **Description**: Padding is the space between the content and the border. It creates an inner spacing around the content area.
- **Properties**: Padding can be set uniformly or individually for each side (top, right, bottom, left) using properties like `padding`, `padding-top`, `padding-right`, `padding-bottom`, and `padding-left`.

#### Example:

```css
.box {
  padding: 20px; /* Uniform padding on all sides */
}
```

#### 3. **Border**

- **Description**: The border surrounds the padding (if any) and content. It can be styled with various widths, colors, and styles (solid, dashed, dotted).
- **Properties**: Borders can be set using properties like `border`, `border-width`, `border-style`, and `border-color`.

#### Example:

```css
.box {
  border: 2px solid black; /* A solid black border */
}
```

#### 4. **Margin**

- **Description**: Margin is the outermost space around the box that separates it from other elements. It creates space outside the border.
- **Properties**: Margins can also be set uniformly or individually for each side using properties like `margin`, `margin-top`, `margin-right`, `margin-bottom`, and `margin-left`.

#### Example:

```css
.box {
  margin: 30px; /* Uniform margin on all sides */
}
```

#### Visual Representation of the Box Model

Here’s a visual representation of how these components fit together:

```
|---------------------------|
|          Margin           |  <-- Outer space around the element
|   |-------------------|   |
|   |      Border       |   |  <-- Surrounds padding and content
|   |   |-----------|   |   |
|   |   |  Padding  |   |   |  <-- Inner space around content
|   |   |           |   |   |
|   |   | Content   |   |   |  <-- Actual content area
|   |   |           |   |   |
|   |   |-----------|   |   |
|   |-------------------|   |
|---------------------------|

```

#### Box Model Calculation

The total width and height of an element can be calculated as follows:

- **Total Width** = Width + Left Padding + Right Padding + Left Border + Right Border + Left Margin + Right Margin
- **Total Height** = Height + Top Padding + Bottom Padding + Top Border + Bottom Border + Top Margin + Bottom Margin

#### Box-Sizing Property

By default, the width and height properties only apply to the content area. However, you can change this behavior using the `box-sizing` property:

- **`content-box`** (default): Width and height include only the content area.
- **`border-box`**: Width and height include padding and border but not margin.

#### Example:

```css
.box {
  box-sizing: border-box; /* Total width includes padding and border */
  width: 200px;
  padding: 20px;
  border: 5px solid black;
}
```

#### Conclusion

The CSS box model is essential for understanding how elements are displayed on a web page. By mastering its components—content, padding, border, and margin—you can effectively control layout, spacing, and overall design in your web projects. Understanding how to manipulate these properties will help you create visually appealing and well-structured web pages.

## 4) Discuss the purpose and usage of CSS selectors. Provide examples of different types of selectors.

**CSS Selectors**: Target HTML elements to apply styles.

- **Purpose**: Select specific HTML elements to apply styles.
- **Usage**: Define styles for targeted elements using selectors.

**Types of Selectors**:

1. **Element Type**: Selects HTML elements by their tag name.
   - Example: `p`, `h1`, `div`
2. **Class**: Selects elements with a specific class attribute.
   - Example: `.button`, `.heading`
3. **ID**: Selects a single element with a unique ID.
   - Example: `#unique-id`
4. **Attribute**: Selects elements based on their attributes.
   - Example: `[target]`, `[target="_blank"]`
5. **Pseudo-class**: Selects elements based on their state or position.
   - Example: `:hover`, `:first-child`, `:nth-child()`
6. **Combinator**: Combines selectors to create complex selection rules.
   - Example: `div p`, `h1 + p`

**Examples**:

- Select all paragraphs: `p { color: blue; }`
- Select elements with class "button": `.button { font-weight: bold; }`
- Select an element with ID "unique-id": `#unique-id { color: red; }`
- Select all links: `a { text-decoration: none; }`
- Select the first paragraph after an `h2` element: `h2 + p { font-style: italic; }`

## 5) How can you apply border radius to an element using CSS3? Provide an example.

You can apply a border radius to an element using the `border-radius` property in CSS3. This property allows you to create rounded corners for any element. You can specify the radius in pixels, percentages, or other length units.

#### Example:

Here’s a simple example of how to use `border-radius` in CSS:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Border Radius Example</title>
    <style>
      .rounded-box {
        width: 200px;
        height: 100px;
        background-color: lightblue;
        border: 2px solid blue;
        border-radius: 20px; /* Apply border radius */
        text-align: center;
        line-height: 100px; /* Center text vertically */
      }
    </style>
  </head>
  <body>
    <div class="rounded-box">Rounded Box</div>
  </body>
</html>
```

#### Explanation:

1. **HTML Structure**:
   - A simple `<div>` element with the class `rounded-box`.
2. **CSS Styles**:
   - **Width and Height**: The box is set to a width of 200px and a height of 100px.
   - **Background Color**: The background is light blue.
   - **Border**: A blue border of 2px.
   - **Border Radius**: The `border-radius: 20px;` property applies rounded corners with a radius of 20 pixels.
   - **Text Centering**: The text inside the box is centered both horizontally and vertically.

You can adjust the value of `border-radius` to achieve different levels of roundness!

## 6) Explain how CSS3 handles background images and gradients. What new properties were introduced for background manipulation?

CSS3 introduced several new features for handling background images and gradients, providing greater flexibility and control over how backgrounds are displayed in web designs. Here's an overview of how CSS3 handles these elements and the new properties introduced:

#### Background Images

1. **Multiple Backgrounds**: CSS3 allows you to set multiple background images for a single element. You can specify them using a comma-separated list.
   - **Example**:
     ```css
     .element {
       background-image: url("image1.jpg"), url("image2.png");
       background-position: top left, bottom right;
       background-repeat: no-repeat, repeat;
     }
     ```
2. **Background Size**: The `background-size` property lets you control the size of the background images. You can set it to specific dimensions or keywords like `cover` and `contain`.
   - **Example**:
     ```css
     .element {
       background-image: url("image.jpg");
       background-size: cover; /* The image covers the entire element */
     }
     ```
3. **Background Attachment**: The `background-attachment` property controls how a background image behaves when scrolling. You can set it to `scroll`, `fixed`, or `local`.
   - **Example**:
     ```css
     .element {
       background-image: url("image.jpg");
       background-attachment: fixed; /* The image stays fixed when scrolling */
     }
     ```

#### Gradients

CSS3 introduced linear and radial gradients as background images, which allow for smooth transitions between colors.

1. **Linear Gradients**: Creates a gradient that transitions along a straight line.
   - **Example**:
     ```css
     .element {
       background: linear-gradient(
         to right,
         red,
         blue
       ); /* Gradient from red to blue */
     }
     ```
2. **Radial Gradients**: Creates a gradient that radiates from a central point.
   - **Example**:
     ```css
     .element {
       background: radial-gradient(
         circle,
         red,
         yellow,
         green
       ); /* Circular gradient */
     }
     ```

#### New Properties for Background Manipulation

1. **`background-image`**: Allows setting one or more background images.
2. **`background-size`**: Specifies the size of the background images. Accepts values like `cover`, `contain`, or specific dimensions (e.g., `100px 100px`).
3. **`background-position`**: Sets the initial position of the background image. You can use keywords (like `top`, `bottom`, `left`, `right`, `center`) or specific coordinates.
4. **`background-repeat`**: Controls how the background image is repeated (e.g., `repeat`, `no-repeat`, `repeat-x`, `repeat-y`).
5. **`background-attachment`**: Determines how the background image behaves when scrolling (`scroll`, `fixed`, `local`).
6. **`background-clip`**: Defines how the background extends within the element's box model (e.g., `border-box`, `padding-box`, `content-box`).
7. **`background-origin`**: Specifies the positioning area of the background image (e.g., `padding-box`, `border-box`, `content-box`).

#### Conclusion

With these new properties and features, CSS3 provides powerful tools for creating visually appealing backgrounds using images and gradients, allowing for a more dynamic and engaging user experience in web design.

## 7) Explain CSS3 transformations and provide examples of how they can be used.

CSS3 transformations allow you to modify the appearance and position of elements in two-dimensional or three-dimensional space. You can use transformations to rotate, scale, translate, and skew elements without affecting the document flow.

#### Types of Transformations

1. **Translate**: Moves an element from its current position.
   - **Example**:
     ```css
     .translate-example {
       transform: translate(
         50px,
         100px
       ); /* Moves the element 50px right and 100px down */
     }
     ```
2. **Scale**: Changes the size of an element.
   - **Example**:
     ```css
     .scale-example {
       transform: scale(1.5); /* Increases the size by 50% */
     }
     ```
3. **Rotate**: Rotates an element around a specified point.
   - **Example**:
     ```css
     .rotate-example {
       transform: rotate(45deg); /* Rotates the element 45 degrees clockwise */
     }
     ```
4. **Skew**: Skews an element along the X and Y axes.
   - **Example**:
     ```css
     .skew-example {
       transform: skew(
         20deg,
         10deg
       ); /* Skews the element 20 degrees horizontally and 10 degrees vertically */
     }
     ```
5. **Combined Transformations**: You can apply multiple transformations at once by separating them with spaces.
   - **Example**:
     ```css
     .combined-example {
       transform: translate(20px, 30px) scale(1.2) rotate(30deg);
     }
     ```

#### 3D Transformations

CSS3 also supports 3D transformations, which include `perspective`, `rotateX`, `rotateY`, and `rotateZ`.

1. **Perspective**: Gives a sense of depth by defining a perspective distance.
   - **Example**:
     ```css
     .perspective-example {
       perspective: 1000px; /* Defines the perspective distance */
     }

     .perspective-box {
       transform: rotateY(45deg); /* Rotates the element in 3D space */
     }
     ```
2. **Rotate in 3D**:
   - **Example**:
     ```css
     .rotate3d-example {
       transform: rotate3d(
         1,
         1,
         0,
         45deg
       ); /* Rotates the element around the X and Y axes */
     }
     ```

#### Transitioning Transformations

You can use transitions to animate transformations smoothly.

- **Example**:
  ```css
  .transition-example {
    transition: transform 0.5s; /* Animation duration */
  }

  .transition-example:hover {
    transform: scale(1.2) rotate(15deg); /* Scale and rotate on hover */
  }
  ```

#### Complete Example

Here’s a complete example combining several transformations:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>CSS3 Transformations Example</title>
    <style>
      .box {
        width: 100px;
        height: 100px;
        background-color: lightcoral;
        margin: 50px;
        transition: transform 0.5s; /* Animation for transformations */
      }

      .box:hover {
        transform: translate(50px, 50px) rotate(45deg) scale(1.5); /* Transformation on hover */
      }
    </style>
  </head>
  <body>
    <div class="box"></div>
  </body>
</html>
```

#### Summary

CSS3 transformations provide a powerful way to manipulate elements visually on a webpage. They enable developers to create dynamic effects, enhance user interactions, and improve overall design aesthetics with minimal effort.

## 8) What are CSS3 transitions, and how do they improve user interaction?

**CSS3 Transitions**: Gradually change element styles over a specified duration.

- **Improve user interaction**:
  - Smoothly animate changes to element styles.
  - Create responsive and engaging user interfaces.
  - Enhance user experience by providing visual feedback.

**Example**:

```css
button {
  transition: background-color 0.5s ease;
}

button:hover {
  background-color: #f00;
}
```

## 9) How do CSS3 animations differ from transitions? Provide an example of each.

**CSS3 Animations vs. Transitions**:

- **Transitions**: Gradually change styles on state change (e.g., hover, focus).
  - Example:
  ```css
  button {
    transition: background-color 0.5s ease;
  }
  button:hover {
    background-color: #f00;
  }
  ```
- **Animations**: Create complex, multi-step animations with keyframes.
  - Example:
  ```css
  @keyframes slide {
    0% {
      transform: translateX(0);
    }
    100% {
      transform: translateX(200px);
    }
  }
  div {
    animation: slide 5s infinite;
  }
  ```
  ## 10) Discuss how CSS3 supports multiple columns in a layout. What properties are used?
  **CSS3 Multi-column Layout**:
  - **Properties**:
    - `column-width`: Set column width.
    - `column-count`: Set number of columns.
    - `column-gap`: Set gap between columns.
    - `column-rule`: Set rule width, style, and color for columns.
  - **Example**:
  ```css
  .container {
    column-width: 200px;
    column-gap: 20px;
    column-rule: 1px solid #000;
  }
  ```

## 11) What are some of the CSS3 user interface features that enhance web design?

- **Transitions**: Smooth state changes.
- **Animations**: Complex, multi-step animations.
- **Transforms**: Visual changes without layout impact.
- **Flexbox**: Responsive, flexible layouts.
- **Grid**: Two-dimensional grid-based layouts.
- **Border-radius**: Rounded corners.
- **Box-shadow**: Drop shadows.
- **Text-shadow**: Text shadows.
- **Background**: Multiple backgrounds, gradients.
- **Border-image**: Custom borders.
- **Pseudo-elements**: Styling content before or after elements.

## 12) What is Bootstrap, and how does it integrate with CSS?

Bootstrap is a popular open-source front-end framework used for designing responsive and mobile-first websites and web applications. It was developed by Twitter and is built on CSS, HTML, and JavaScript. Bootstrap provides a collection of pre-defined classes, components, and JavaScript plugins that help developers create responsive layouts, forms, buttons, navigation, and other UI elements with minimal effort.

Here's how Bootstrap integrates with CSS:

1. **Responsive Design**: Bootstrap uses a responsive design approach, which means it automatically adjusts the layout and styling of a web page based on the device's screen size. This is achieved using CSS media queries and a responsive grid system. The grid system is built on a 12-column layout, which can be further customized to create complex layouts.
2. **CSS Preprocessors**: Bootstrap supports CSS preprocessors like Less and Sass, which allow developers to write CSS in a more efficient and maintainable way. These preprocessors enable features like variables, mixins, and nesting, which can be compiled into regular CSS.
3. **Customization**: Bootstrap allows for easy customization of its CSS. You can customize variables, maps, and mixins in the source Less or Sass files, or use the Bootstrap customizer tool to generate a custom CSS file with your desired settings.
4. **CSS Utility Classes**: Bootstrap provides a set of utility classes that can be used to quickly apply styles to HTML elements. These classes are based on CSS and can be used to control spacing, alignment, color, and more. For example, you can use `.text-center` to center text, or `.mt-3` to add margin-top of 1rem.
5. **Components**: Bootstrap includes a wide range of pre-built components, such as buttons, cards, navbars, and modals, which are styled using CSS. These components can be easily integrated into your project by adding the necessary CSS and HTML.

Here's a simple example of how Bootstrap integrates with CSS to create a button:

```html
<!-- HTML -->
<button type="button" class="btn btn-primary">Button</button>
```

```css
/* CSS (from Bootstrap's source files) */
.btn {
  display: inline-block;
  font-weight: 400;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  border: 1px solid transparent;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.5;
  border-radius: 0.25rem;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out,
    border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

.btn-primary {
  color: #fff;
  background-color: #007bff;
  border-color: #007bff;
}
```

In this example, the `.btn` class applies basic button styles, while the `.btn-primary` class applies the specific styles for a primary button, including color, background color, and border color.

## 13) What is JavaScript, and how does it enhance web page functionality?

JavaScript is a programming language used to make web pages interactive and dynamic. It runs in the browser and allows you to add functionality to your web pages that plain HTML and CSS cannot achieve alone.

#### How JavaScript Enhances Web Page Functionality:

1. **Interactivity:**
   - **User Input:** JavaScript can respond to user actions like clicks, mouse movements, and key presses.
   - **Dynamic Content:** It can change the content of a web page without reloading the entire page.
2. **Animation and Effects:**
   - JavaScript can create animations, transitions, and other visual effects to make web pages more engaging.
3. **Form Validation:**
   - It can check user input in forms before sending it to the server, ensuring data is correct and complete.
4. **Asynchronous Operations:**
   - JavaScript allows for asynchronous operations, such as fetching data from a server without interrupting the user experience.
5. **Integration with APIs:**
   - It can interact with web APIs to fetch and display data from external sources, like social media feeds or weather updates.

#### Example of JavaScript in Action:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>JavaScript Example</title>
  </head>
  <body>
    <button onclick="changeText()">Click Me!</button>
    <p id="text">Hello, World!</p>

    <script>
      function changeText() {
        document.getElementById("text").innerText = "Text Changed!";
      }
    </script>
  </body>
</html>
```

In this example, clicking the button changes the text of a paragraph, demonstrating how JavaScript can make a web page interactive.

## 14) What is JS Variable? Explain the different ways to declare variables in JavaScript. Provide examples.

A JavaScript variable is a container that stores data values. You can think of it as a box where you can put different types of data, like numbers, text, or objects.

#### Ways to Declare Variables in JavaScript:

1. **Using `var`:**

   - `var` is the oldest way to declare variables.
   - It has function scope, meaning it is accessible within the function it is declared in.

   ```jsx
   var x = 10;
   console.log(x); // Outputs: 10
   ```

2. **Using `let`:**

   - `let` is introduced in ES6 and has block scope, meaning it is accessible only within the block (e.g., loop, if statement) it is declared in.

   ```jsx
   let y = 20;
   console.log(y); // Outputs: 20
   ```

3. **Using `const`:**

   - `const` is also introduced in ES6 and is used to declare constants, which cannot be reassigned.
   - It also has block scope.

   ```jsx
   const z = 30;
   console.log(z); // Outputs: 30
   ```

#### Example Comparing Scope:

```jsx
function example() {
  if (true) {
    var a = 5; // Accessible outside the if block
    let b = 10; // Not accessible outside the if block
    const c = 15; // Not accessible outside the if block
  }
  console.log(a); // Outputs: 5
  // console.log(b); // Error: b is not defined
  // console.log(c); // Error: c is not defined
}

example();
```

In this example, `var a` is accessible outside the if block, but `let b` and `const c` are not, demonstrating the difference in scope between `var`, `let`, and `const`.

## 15) How do conditional statements work in JavaScript? Provide examples of if, else if, and switch statements.

Conditional statements in JavaScript allow you to execute different blocks of code based on certain conditions. Here are the main types:

1. **if statement:**

   - Executes a block of code if a specified condition is true.

   ```jsx
   let score = 85;
   if (score >= 90) {
     console.log("Grade: A");
   }
   ```

2. **if...else statement:**

   - Executes one block of code if the condition is true, and another block if the condition is false.

   ```jsx
   let score = 85;
   if (score >= 90) {
     console.log("Grade: A");
   } else {
     console.log("Grade: B");
   }
   ```

3. **else if statement:**

   - Allows you to check multiple conditions.

   ```jsx
   let score = 75;
   if (score >= 90) {
     console.log("Grade: A");
   } else if (score >= 80) {
     console.log("Grade: B");
   } else if (score >= 70) {
     console.log("Grade: C");
   } else {
     console.log("Grade: D");
   }
   ```

4. **switch statement:**

   - Executes one block of code among many, based on the value of a variable.

   ```jsx
   let day = 3;
   switch (day) {
     case 1:
       console.log("Monday");
       break;
     case 2:
       console.log("Tuesday");
       break;
     case 3:
       console.log("Wednesday");
       break;
     default:
       console.log("Other day");
   }
   ```

In each example, the code inside the conditional block is executed only if the condition is met. The `switch` statement uses the `case` keyword to check for specific values and the `break` keyword to exit the switch block once a match is found.

## 16) Describe how looping constructs like for, while, and do...while work in JavaScript. Provide examples.

Looping constructs in JavaScript allow you to execute a block of code repeatedly based on a given condition. Here are the main types:

1. **for loop:**

   - Executes a block of code a specific number of times.

   ```jsx
   for (let i = 0; i < 5; i++) {
     console.log(i); // Outputs: 0, 1, 2, 3, 4
   }
   ```

2. **while loop:**

   - Executes a block of code as long as a specified condition is true.

   ```jsx
   let i = 0;
   while (i < 5) {
     console.log(i); // Outputs: 0, 1, 2, 3, 4
     i++;
   }
   ```

3. **do...while loop:**

   - Similar to the while loop, but ensures the block of code is executed at least once before checking the condition.

   ```jsx
   let i = 0;
   do {
     console.log(i); // Outputs: 0, 1, 2, 3, 4
     i++;
   } while (i < 5);
   ```

#### Key Differences:

- **for loop**: Useful when you know the number of iterations beforehand.
- **while loop**: Useful when the number of iterations depends on a condition that may change during execution.
- **do...while loop**: Ensures the code block runs at least once before checking the condition.

These loops help automate repetitive tasks and are essential for tasks like iterating over arrays, generating sequences, and more.

## 17) What are JavaScript functions, and how do you define and call them?

JavaScript functions are reusable blocks of code that perform a specific task. They help organize your code and make it more modular.

#### Defining a Function:

1. **Named Function:**

   ```jsx
   function greet(name) {
     return "Hello, " + name + "!";
   }
   ```

2. **Anonymous Function (using a variable):**

   ```jsx
   const greet = function (name) {
     return "Hello, " + name + "!";
   };
   ```

3. **Arrow Function (introduced in ES6):**

   ```jsx
   const greet = (name) => {
     return "Hello, " + name + "!";
   };
   ```

#### Calling a Function:

```jsx
let message = greet("Alice"); // Calls the function and stores the result in 'message'
console.log(message); // Outputs: Hello, Alice!
```

Functions can take inputs (called parameters) and return an output value. In the examples above, `name` is a parameter, and `'Hello, ' + name + '!'` is the return value.

## 18) How can you handle events in JavaScript? Provide examples of event handling.

Handling events in JavaScript allows you to respond to user actions, such as clicks, key presses, and form submissions. Here's how you can handle events:

#### 1. Inline Event Handlers:

You can add event handlers directly in the HTML.

```html
<button onclick="alert('Button clicked!')">Click Me</button>
```

#### 2. Assigning Event Handlers Using JavaScript:

You can assign event handlers using JavaScript to keep your HTML clean.

```html
<button id="myButton">Click Me</button>

<script>
  document.getElementById("myButton").onclick = function () {
    alert("Button clicked!");
  };
</script>
```

#### 3. Using `addEventListener`:

The `addEventListener` method allows you to add multiple event handlers to a single element.

```html
<button id="myButton">Click Me</button>

<script>
  document.getElementById("myButton").addEventListener("click", function () {
    alert("Button clicked!");
  });
</script>
```

#### 4. Handling Multiple Events:

You can handle multiple events on the same element.

```html
<input type="text" id="myInput" placeholder="Type something..." />

<script>
  const input = document.getElementById("myInput");

  input.addEventListener("focus", function () {
    console.log("Input focused");
  });

  input.addEventListener("blur", function () {
    console.log("Input blurred");
  });
</script>
```

#### 5. Removing Event Listeners:

You can also remove event listeners when they are no longer needed.

```html
<button id="myButton">Click Me</button>

<script>
  const button = document.getElementById("myButton");

  function handleClick() {
    alert("Button clicked!");
    button.removeEventListener("click", handleClick);
  }

  button.addEventListener("click", handleClick);
</script>
```

These examples cover different ways to handle events in JavaScript, from inline event handlers to using `addEventListener` for more flexibility and control.

## 19) What are cookies in JavaScript, and how can they be used to store information?

Cookies in JavaScript are small text files stored on a user's browser by a website. They are used to store information such as user preferences, login status, and session data.

#### How to Use Cookies:

1. **Setting a Cookie:**

   ```jsx
   document.cookie =
     "username=JohnDoe; expires=Fri, 31 Dec 2023 23:59:59 GMT; path=/";
   ```

2. **Reading a Cookie:**

   ```jsx
   function getCookie(name) {
     let cookieArray = document.cookie.split(";");
     for (let i = 0; i < cookieArray.length; i++) {
       let cookie = cookieArray[i].trim();
       if (cookie.startsWith(name + "=")) {
         return cookie.substring(name.length + 1);
       }
     }
     return null;
   }

   let username = getCookie("username");
   console.log(username); // Outputs: JohnDoe
   ```

3. **Deleting a Cookie:**

   ```jsx
   document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/";
   ```

#### Key Points:

- **Name-Value Pairs:** Cookies store data as name-value pairs.
- **Expiration Date:** You can set an expiration date to control how long the cookie is stored.
- **Path:** The path attribute specifies the path where the cookie is valid.

Cookies are useful for storing small amounts of data on the client side, but they have limitations in size and can be less secure compared to server-side storage.

## 20) What are JavaScript objects, and how are they used to structure data? Provide examples.

JavaScript objects are collections of key-value pairs, used to structure and organize data. They allow you to group related data and functions together.

#### Creating an Object:

```jsx
let person = {
  firstName: "John",
  lastName: "Doe",
  age: 30,
  isStudent: false,
  greet: function () {
    return "Hello, " + this.firstName + " " + this.lastName;
  },
};
```

#### Accessing Object Properties:

- **Dot Notation:**
  ```jsx
  console.log(person.firstName); // Outputs: John
  ```
- **Bracket Notation:**
  ```jsx
  console.log(person["lastName"]); // Outputs: Doe
  ```

#### Adding or Modifying Properties:

```jsx
person.age = 31; // Modifies age
person.city = "New York"; // Adds a new property
```

#### Deleting Properties:

```jsx
delete person.isStudent; // Deletes the isStudent property
```

#### Using Methods:

```jsx
console.log(person.greet()); // Outputs: Hello, John Doe
```

#### Example of Nested Objects:

```jsx
let user = {
  name: "Jane",
  address: {
    street: "123 Main St",
    city: "Anytown",
  },
};

console.log(user.address.city); // Outputs: Anytown
```

Objects in JavaScript are versatile and can contain various data types, including other objects. They are essential for structuring complex data and making your code more organized and readable.

## 21) Explain error handling in JavaScript. What methods are available for handling errors?

Error handling in JavaScript is crucial for managing and responding to runtime errors gracefully. It helps in maintaining the flow of the program and providing meaningful feedback to users.

#### Methods for Handling Errors:

1. **try...catch Statement:**

   - The `try` block contains code that may throw an exception.
   - The `catch` block handles the exception.

   ```jsx
   try {
     let result = 10 / 0; // This will throw an error
   } catch (error) {
     console.log("An error occurred: " + error.message);
   }
   ```

2. **throw Statement:**

   - You can throw your own exceptions using the `throw` statement.

   ```jsx
   function checkAge(age) {
     if (age < 18) {
       throw new Error("You must be at least 18 years old");
     }
   }

   try {
     checkAge(15);
   } catch (error) {
     console.log(error.message); // Outputs: You must be at least 18 years old
   }
   ```

3. **finally Block:**

   - The `finally` block contains code that will execute regardless of whether an error occurred or not.

   ```jsx
   try {
     let result = 10 / 0;
   } catch (error) {
     console.log("An error occurred: " + error.message);
   } finally {
     console.log("This will always run");
   }
   ```

4. **Error Object:**

   - JavaScript has a built-in `Error` object that provides information about the error.

   ```jsx
   try {
     throw new Error("Something went wrong");
   } catch (error) {
     console.log(error.name); // Outputs: Error
     console.log(error.message); // Outputs: Something went wrong
     console.log(error.stack); // Outputs: stack trace
   }
   ```

#### Best Practices:

- Use `try...catch` blocks to handle potential errors.
- Use `throw` to create custom errors when needed.
- Use `finally` for cleanup code that must run regardless of errors.
- Provide meaningful error messages to help with debugging.

By using these methods, you can handle errors effectively and make your JavaScript code more robust and user-friendly.

## 22) How can you validate user input using JavaScript? Provide examples of common validation techniques.

Validating user input using JavaScript ensures that the data entered by users is correct and secure. Here are some common validation techniques:

#### 1. Checking for Empty Fields:

Ensure that required fields are not left empty.

```jsx
function validateName(name) {
  if (name.trim() === "") {
    return "Name is required";
  }
  return "";
}

let name = prompt("Enter your name:");
let error = validateName(name);
if (error) {
  alert(error);
}
```

#### 2. Validating Email Address:

Use a regular expression to check the format of an email address.

```jsx
function validateEmail(email) {
  const regex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
  if (!regex.test(email)) {
    return "Invalid email address";
  }
  return "";
}

let email = prompt("Enter your email:");
let error = validateEmail(email);
if (error) {
  alert(error);
}
```

#### 3. Validating Numeric Input:

Ensure that a value is a number and within a specific range.

```jsx
function validateAge(age) {
  if (isNaN(age) || age < 1 || age > 120) {
    return "Invalid age";
  }
  return "";
}

let age = prompt("Enter your age:");
let error = validateAge(age);
if (error) {
  alert(error);
}
```

#### 4. Validating Password Strength:

Check for minimum length and inclusion of special characters.

```jsx
function validatePassword(password) {
  if (password.length < 8) {
    return "Password must be at least 8 characters long";
  }
  if (!/[A-Z]/.test(password)) {
    return "Password must contain at least one uppercase letter";
  }
  if (!/[0-9]/.test(password)) {
    return "Password must contain at least one number";
  }
  return "";
}

let password = prompt("Enter your password:");
let error = validatePassword(password);
if (error) {
  alert(error);
}
```

#### 5. Validating Date Format:

Ensure that a date is in the correct format (e.g., MM/DD/YYYY).

```jsx
function validateDate(date) {
  const regex = /^(0[1-9]|1[0-2])\\/(0[1-9]|[12][0-9]|3[01])\\/(19|20)\\d\\d$/;
  if (!regex.test(date)) {
    return "Invalid date format (MM/DD/YYYY)";
  }
  return "";
}

let date = prompt("Enter a date (MM/DD/YYYY):");
let error = validateDate(date);
if (error) {
  alert(error);
}

```

These examples demonstrate common techniques for validating user input in JavaScript. Using regular expressions and conditional checks, you can ensure that the data entered by users meets the required criteria.

## 23) Discuss how JavaScript can be used for animations. What libraries or methods are commonly used?

JavaScript can be used to create animations on web pages, making them more interactive and engaging. Here are some common methods and libraries for creating animations with JavaScript:

#### 1. **CSS Animations with JavaScript:**

You can use JavaScript to trigger CSS animations. This approach leverages the power of CSS for smooth animations while using JavaScript for control.

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      @keyframes move {
        from {
          transform: translateX(0);
        }
        to {
          transform: translateX(100px);
        }
      }
      .box {
        width: 50px;
        height: 50px;
        background-color: red;
      }
      .animate {
        animation: move 2s infinite;
      }
    </style>
  </head>
  <body>
    <div class="box" id="box"></div>
    <button onclick="startAnimation()">Start Animation</button>

    <script>
      function startAnimation() {
        document.getElementById("box").classList.add("animate");
      }
    </script>
  </body>
</html>
```

#### 2. **Using `requestAnimationFrame`:**

This method provides a way to perform smooth animations by calling a function before the browser repaints.

```jsx
let start = null;
const element = document.getElementById("box");

function animate(timestamp) {
  if (!start) start = timestamp;
  const progress = timestamp - start;
  element.style.transform = `translateX(${Math.min(progress / 10, 200)}px)`;
  if (progress < 2000) {
    // Stop after 2 seconds
    requestAnimationFrame(animate);
  }
}

requestAnimationFrame(animate);
```

#### 3. **Libraries for Animations:**

- **jQuery:** A popular library that simplifies DOM manipulation and animations.
  ```jsx
  $("#box").animate({ left: "100px" }, 2000);
  ```
- **GSAP (GreenSock Animation Platform):** A powerful library for high-performance animations.
  ```jsx
  gsap.to("#box", { x: 100, duration: 2 });
  ```
- **Anime.js:** A lightweight and flexible library for CSS animations.
  ```jsx
  anime({
    targets: "#box",
    translateX: 100,
    duration: 2000,
  });
  ```

#### 4. **Canvas API:**

For more complex animations, you can use the HTML5 Canvas API.

```html
<canvas id="canvas" width="400" height="400"></canvas>

<script>
  const canvas = document.getElementById("canvas");
  const ctx = canvas.getContext("2d");

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "red";
    ctx.fillRect(10, 10, 50, 50);
    requestAnimationFrame(draw);
  }

  draw();
</script>
```

These methods and libraries make it easy to create a variety of animations, from simple movements to complex interactive effects. Using JavaScript for animations can greatly enhance the user experience on your web pages.

## 24) What role does JavaScript play in handling multimedia content on a web page? Provide examples of how JavaScript can interact with audio and video elements.

JavaScript plays a crucial role in handling multimedia content on a web page by enabling dynamic interaction and control over audio and video elements. Here are some examples of how JavaScript can interact with multimedia:

#### Controlling Audio Playback:

You can use JavaScript to play, pause, and stop audio files.

```html
<audio id="myAudio" src="audio.mp3"></audio>
<button onclick="playAudio()">Play</button>
<button onclick="pauseAudio()">Pause</button>

<script>
  const audio = document.getElementById("myAudio");

  function playAudio() {
    audio.play();
  }

  function pauseAudio() {
    audio.pause();
  }
</script>
```

#### Controlling Video Playback:

JavaScript can also control video elements, such as playing, pausing, and adjusting the volume.

```html
<video id="myVideo" width="320" height="240" controls>
  <source src="video.mp4" type="video/mp4" />
</video>
<button onclick="playVideo()">Play</button>
<button onclick="pauseVideo()">Pause</button>

<script>
  const video = document.getElementById("myVideo");

  function playVideo() {
    video.play();
  }

  function pauseVideo() {
    video.pause();
  }
</script>
```

#### Adjusting Volume:

You can use JavaScript to adjust the volume of audio and video elements.

```html
<audio id="myAudio" src="audio.mp3" controls></audio>
<input type="range" id="volumeControl" min="0" max="1" step="0.1" />

<script>
  const audio = document.getElementById("myAudio");
  const volumeControl = document.getElementById("volumeControl");

  volumeControl.addEventListener("input", function () {
    audio.volume = volumeControl.value;
  });
</script>
```

#### Handling Events:

JavaScript can handle events like `play`, `pause`, and `ended` to perform actions when these events occur.

```html
<video id="myVideo" width="320" height="240" controls>
  <source src="video.mp4" type="video/mp4" />
</video>

<script>
  const video = document.getElementById("myVideo");

  video.addEventListener("play", function () {
    console.log("Video started playing");
  });

  video.addEventListener("pause", function () {
    console.log("Video paused");
  });

  video.addEventListener("ended", function () {
    console.log("Video ended");
  });
</script>
```

These examples show how JavaScript can interact with audio and video elements to control playback, adjust volume, and handle events. This makes multimedia content on web pages more dynamic and interactive.

## 25) What is the difference between inline, embedded and external style sheets?

Sure, let's break down the differences between inline, embedded, and external style sheets in a simple and memorable way:

#### Inline Style Sheets:

- **Definition:** Inline styles are applied directly to individual HTML elements using the `style` attribute.
- **Usage:** `<p style="color: blue; font-size: 16px;">This is a paragraph.</p>`
- **Pros:** Quick and easy for small changes.
- **Cons:** Hard to manage for larger projects; can clutter the HTML.

#### Embedded Style Sheets:

- **Definition:** Embedded styles are defined within the `<style>` tag inside the HTML `<head>` section.
- **Usage:**
  ```html
  <head>
    <style>
      p {
        color: blue;
        font-size: 16px;
      }
    </style>
  </head>
  <body>
    <p>This is a paragraph.</p>
  </body>
  ```
- **Pros:** Easier to manage than inline styles; styles can be applied to multiple elements.
- **Cons:** Still within the HTML file, which can make it messy for large projects.

#### External Style Sheets:

- **Definition:** External styles are defined in a separate CSS file and linked to the HTML document using the `<link>` tag.
- **Usage:**
  ```html
  <!-- HTML File -->
  <head>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <p>This is a paragraph.</p>
  </body>
  ```
  ```css
  /* styles.css */
  p {
    color: blue;
    font-size: 16px;
  }
  ```
- **Pros:** Best for large projects; keeps HTML clean; reusable across multiple pages.
- **Cons:** Requires an additional file; may have slight loading delays.

#### Summary:

- **Inline:** Directly in HTML elements, quick but messy.
- **Embedded:** Inside the HTML `<head>`, better for small to medium projects.
- **External:** Separate CSS file, best for large projects and clean HTML.

Each type has its use cases, but external style sheets are generally preferred for larger projects due to their maintainability and reusability.

## 26) Write CSS code to set proper design of registration page that contain

a. following data fields (Student enrol no, student name, Student mobile no,
b. student email id, branch, semester).

Certainly! Below is an example of CSS code to style a registration page containing the specified data fields:

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
      }

      .registration-form {
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        width: 300px;
      }

      .registration-form h2 {
        text-align: center;
        margin-bottom: 20px;
      }

      .registration-form label {
        display: block;
        margin-bottom: 5px;
        font-weight: bold;
      }

      .registration-form input {
        width: 100%;
        padding: 10px;
        margin-bottom: 20px;
        border: 1px solid #ccc;
        border-radius: 4px;
      }

      .registration-form button {
        width: 100%;
        padding: 10px;
        background-color: #4caf50;
        color: #fff;
        border: none;
        border-radius: 4px;
        cursor: pointer;
      }

      .registration-form button:hover {
        background-color: #45a049;
      }
    </style>
  </head>
  <body>
    <div class="registration-form">
      <h2>Student Registration</h2>
      <form>
        <label for="enrolNo">Student Enrol No.</label>
        <input type="text" id="enrolNo" name="enrolNo" required />

        <label for="name">Student Name</label>
        <input type="text" id="name" name="name" required />

        <label for="mobileNo">Student Mobile No.</label>
        <input type="text" id="mobileNo" name="mobileNo" required />

        <label for="email">Student Email ID</label>
        <input type="email" id="email" name="email" required />

        <label for="branch">Branch</label>
        <input type="text" id="branch" name="branch" required />

        <label for="semester">Semester</label>
        <input type="text" id="semester" name="semester" required />

        <button type="submit">Register</button>
      </form>
    </div>
  </body>
</html>
```

This CSS code styles a registration form for students, including fields for enrollment number, name, mobile number, email ID, branch, and semester. The form is centered on the page with a clean, modern design.

## 27) What is Margin and padding? How can it be used in web page designing?

Sure, let's break down margin and padding in a simple and memorable way:

#### Margin:

- **Definition:** Margin is the space outside of an element, between the element and its neighboring elements.
- **Usage:** Controls the space around an element, pushing other elements away.
- **CSS Property:** `margin`
  - `margin-top`, `margin-right`, `margin-bottom`, `margin-left` for specific sides.
  - Shorthand: `margin: top right bottom left;`
- **Example:**
  ```css
  .box {
    margin: 20px; /* All sides */
    margin-top: 10px; /* Top side only */
  }
  ```

#### Padding:

- **Definition:** Padding is the space inside an element, between the content and the border.
- **Usage:** Controls the space within an element, pushing the content away from the border.
- **CSS Property:** `padding`
  - `padding-top`, `padding-right`, `padding-bottom`, `padding-left` for specific sides.
  - Shorthand: `padding: top right bottom left;`
- **Example:**
  ```css
  .box {
    padding: 20px; /* All sides */
    padding-left: 10px; /* Left side only */
  }
  ```

#### How to Use in Web Page Designing:

- **Margin:** Use margin to create space between elements, ensuring they don't overlap or look cramped.
  ```css
  .header {
    margin-bottom: 20px; /* Space below the header */
  }
  ```
- **Padding:** Use padding to add space inside elements, making the content look more comfortable and readable.
  ```css
  .button {
    padding: 10px 20px; /* Space inside the button */
  }
  ```

#### Summary:

- **Margin:** Space outside the element, between it and other elements.
- **Padding:** Space inside the element, between the content and the border.

Both margin and padding are crucial for creating well-spaced, visually appealing web pages. They help ensure that elements have enough breathing room and that content is nicely padded within its containers.

## 28) Write a program using HTML and CSS to change the background colour of a <div> on a mouse over event.

Sure! Below is a simple example of how to change the background color of a `<div>` element when the mouse hovers over it using HTML and CSS:

#### HTML:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Change Background Color on Hover</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <div class="hover-box">Hover over me!</div>
  </body>
</html>
```

#### CSS (styles.css):

```css
.hover-box {
  width: 200px;
  height: 100px;
  border: 1px solid #000;
  text-align: center;
  line-height: 100px;
  transition: background-color 0.3s; /* Smooth transition */
}

.hover-box:hover {
  background-color: yellow;
}
```

#### Explanation:

1. **HTML:**
   - The HTML file contains a `<div>` element with the class `hover-box`.
2. **CSS:**
   - The `.hover-box` class styles the `<div>` with a specific width, height, border, and text alignment.
   - The `transition` property is used to make the background color change smoothly.
   - The `.hover-box:hover` selector changes the background color of the `<div>` to yellow when the mouse hovers over it.

This simple example demonstrates how to use CSS to change the background color of a `<div>` element on a mouse hover event. The `transition` property is added to make the background color change smoothly.

## 29) What is the use of position property in css? Explain different values of position property.

Certainly! The `position` property in CSS is used to define the positioning behavior of an element. It allows you to control the placement of elements on a web page.

#### Different Values of the `position` Property:

1. **static:**

   - **Default Value:** Elements are positioned according to the normal flow of the document.
   - **Usage:** No special positioning is applied.

   ```css
   .static-box {
     position: static;
   }
   ```

2. **relative:**

   - **Description:** Elements are positioned relative to their normal position.
   - **Usage:** You can use `top`, `right`, `bottom`, and `left` to adjust the position.

   ```css
   .relative-box {
     position: relative;
     top: 20px;
     left: 20px;
   }
   ```

3. **absolute:**

   - **Description:** Elements are positioned relative to the nearest positioned (non-static) ancestor.
   - **Usage:** Useful for creating overlays and positioning elements precisely.

   ```css
   .absolute-box {
     position: absolute;
     top: 50px;
     left: 50px;
   }
   ```

4. **fixed:**

   - **Description:** Elements are positioned relative to the viewport, which means they stay in the same place even when the page is scrolled.
   - **Usage:** Commonly used for navigation bars and footers.

   ```css
   .fixed-box {
     position: fixed;
     top: 10px;
     right: 10px;
   }
   ```

5. **sticky:**

   - **Description:** Elements are positioned based on the user's scroll position. It toggles between relative and fixed, depending on the scroll position.
   - **Usage:** Useful for creating sticky headers or navigation bars.

   ```css
   .sticky-box {
     position: sticky;
     top: 0;
   }
   ```

#### Summary:

- **static:** Default positioning.
- **relative:** Positioned relative to its normal position.
- **absolute:** Positioned relative to the nearest positioned ancestor.
- **fixed:** Positioned relative to the viewport.
- **sticky:** Positioned based on the user's scroll position.

Each value of the `position` property serves a specific purpose, allowing you to control the layout and behavior of elements on your web page effectively.

## 30) How to create a hyperlink in HTML? Explain all pseudo classes of hyperlink in detail.

Certainly! Creating a hyperlink in HTML is straightforward. Here's how you can do it, along with an explanation of the pseudo-classes of hyperlinks.

#### Creating a Hyperlink:

To create a hyperlink, you use the `<a>` (anchor) tag with the `href` attribute specifying the URL.

```html
<a href="<https://www.example.com>">Visit Example</a>
```

#### Pseudo-Classes of Hyperlinks:

Pseudo-classes are used to define the styles of hyperlinks based on their state. Here are the main pseudo-classes:

1. **:link**

   - **Description:** Applies to links that have not been visited.
   - **Usage:** Styles unvisited links.

   ```css
   a:link {
     color: blue;
     text-decoration: none;
   }
   ```

2. **:visited**

   - **Description:** Applies to links that have been visited.
   - **Usage:** Styles visited links.

   ```css
   a:visited {
     color: purple;
     text-decoration: none;
   }
   ```

3. **:hover**

   - **Description:** Applies to links when the user hovers over them.
   - **Usage:** Styles links when the mouse pointer is over them.

   ```css
   a:hover {
     color: red;
     text-decoration: underline;
   }
   ```

4. **:active**

   - **Description:** Applies to links when they are being activated (e.g., clicked).
   - **Usage:** Styles links when they are clicked.

   ```css
   a:active {
     color: green;
     text-decoration: underline;
   }
   ```

#### Example:

Here’s a complete example putting it all together:

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      a:link {
        color: blue;
        text-decoration: none;
      }
      a:visited {
        color: purple;
        text-decoration: none;
      }
      a:hover {
        color: red;
        text-decoration: underline;
      }
      a:active {
        color: green;
        text-decoration: underline;
      }
    </style>
  </head>
  <body>
    <a href="<https://www.example.com>">Visit Example</a>
  </body>
</html>
```

#### Summary:

- **Creating a Hyperlink:** Use the `<a>` tag with the `href` attribute.
- **Pseudo-Classes:**
  - `:link`: Styles unvisited links.
  - `:visited`: Styles visited links.
  - `:hover`: Styles links when hovered over.
  - `:active`: Styles links when clicked.

These pseudo-classes help you create interactive and visually appealing hyperlinks on your web page.

## 31) Discuss pseudo class and pseudo element with examples.

**Pseudo-classes and Pseudo-elements in CSS:**

**Pseudo-classes** style elements based on their state, while **pseudo-elements** represent abstract or virtual elements that aren't physically present in the HTML.

**Pseudo-classes:**

- Style links based on their state:
  - `:link`: Unvisited link (blue)
  - `:visited`: Visited link (purple)
  - `:hover`: Link on hover (underline)
  - `:active`: Link being clicked (yellow background)
  - `:focus`: Link with focus (red outline)

Example:

```css
a:link {
  color: blue;
}
a:visited {
  color: purple;
}
a:hover {
  text-decoration: underline;
}
a:active {
  background-color: yellow;
}
a:focus {
  outline: 2px solid red;
}
```

**Pseudo-elements:**

- `::before`: Insert content before an element's content.
  - Example: `p::before { content: "📝 "; }` (Adds a note icon before paragraph text)
- `::after`: Insert content after an element's content.
  - Example: `p::after { content: " 🌟"; }` (Adds a star after paragraph text)
- `::first-line`: Select the first line of a block-level element.
  - Example: `p::first-line { font-size: 1.5em; }` (Makes the first line of a paragraph larger)
- `::marker`: Select the marker box of a list item.
  - Example: `li::marker { color: red; }` (Changes the color of list item markers)
- `::selection`: Select the part of an element that is selected by the user.
  - Example: `p::selection { background-color: yellow; }` (Highlights selected text in yellow)

Example:

```css
p::before {
  content: "📝 ";
}
p::after {
  content: " 🌟";
}
p::first-line {
  font-size: 1.5em;
}
li::marker {
  color: red;
}
p::selection {
  background-color: yellow;
}
```

## 32) What are JavaScript Data Types? What is the use of the NaN function?

**JavaScript Data Types:**

JavaScript has six primitive data types and one non-primitive (object) data type:

1. **Number:** Represents numeric values, both integers and floating-point numbers.
   - Example: `let x = 42;`
2. **String:** Represents textual data.
   - Example: `let name = "John Doe";`
3. **Boolean:** Represents logical values: true or false.
   - Example: `let isStudent = true;`
4. **Null:** Represents an empty value or no value.
   - Example: `let empty = null;`
5. **Undefined:** Represents a variable that has not been assigned a value.
   - Example: `let y;`
6. **Symbol (ES6):** Represents unique and immutable values, often used as object keys.
   - Example: `let sym = Symbol("description");`
7. **Object:** Represents complex data structures, collections of key-value pairs.
   - Example: `let person = { name: "John", age: 30 };`

**Use of the `NaN` function:**

`NaN` stands for "Not a Number" and is a special numeric value that represents an invalid or undefined mathematical operation result. The `NaN` function returns the `NaN` value.

Here's why `NaN` is useful:

- **Checking for invalid numbers:** You can use `NaN` to check if a value is a valid number or not.
  - Example: `console.log(Number("hello") === NaN); // true`
- **Avoiding mathematical errors:** By checking for `NaN`, you can prevent your code from throwing errors due to invalid mathematical operations.
  - Example:
    ```jsx
    let x = 10 / "2";
    if (isNaN(x)) {
      console.log("Invalid operation");
    } else {
      console.log(x);
    }
    ```
- **Comparing with `NaN`:** Comparing with `NaN` using the strict equality operator (`===`) always returns `false`. To check if a value is `NaN`, use the `isNaN()` function.
  - Example: `console.log(NaN === NaN); // false`
  - Example: `console.log(isNaN(NaN)); // true`

## 33) What are global variables? How are these variables declared and what are the problems associated with using them?

**Global Variables in JavaScript:**

Global variables are variables declared outside of any function or block, making them accessible throughout the entire script or even across different scripts.

**Declaring Global Variables:**

1. **At the top level of your script:**

   ```jsx
   let globalVar = "I am a global variable";
   ```

2. **Using the `window` object:**

   ```jsx
   window.globalVar = "I am a global variable";
   ```

**Problems Associated with Using Global Variables:**

1. **Name collisions:** Global variables can overwrite or be overwritten by other scripts or libraries, leading to unexpected behavior.
   - Example:
     ```jsx
     // Script 1
     let user = "John Doe";

     // Script 2
     let user = "Jane Doe"; // Overwrites the global user variable from Script 1
     ```
2. **Tight coupling:** Global variables create tight coupling between different parts of your code, making it harder to maintain, test, and reuse your code.
   - Example:
     ```jsx
     // Function A uses globalVar
     function A() {
       console.log(globalVar);
     }

     // Function B changes globalVar
     function B() {
       globalVar = "New value";
     }
     ```
3. **Inaccessibility in modules:** Global variables are not accessible inside modules (ES6) or IIFE (Immediately Invoked Function Expression) closures.
   - Example:
     ```jsx
     // Global variable
     let globalVar = "I am a global variable";

     // Module
     (() => {
       console.log(globalVar); // ReferenceError: globalVar is not defined
     })();
     ```

To avoid these problems, consider using function-scoped or module-scoped variables instead of global variables.

## 34) What is 'this' keyword in JavaScript?

**The 'this' Keyword in JavaScript:**

The `this` keyword in JavaScript refers to an object, and its value depends on how it's used:

1. **In a function:** `this` refers to the global object (`window` in browsers) if the function is called as a standalone function.
   - Example:
     ```jsx
     function foo() {
       console.log(this);
     }
     foo(); // logs Window {}
     ```
2. **As a method of an object:** `this` refers to the object that the method is called on.
   - Example:
     ```jsx
     const obj = {
       name: "John",
       sayName: function () {
         console.log(this.name);
       },
     };
     obj.sayName(); // logs "John"
     ```
3. **With a constructor function:** `this` refers to the newly created object.
   - Example:
     ```jsx
     function Person(name) {
       this.name = name;
     }
     const john = new Person("John");
     console.log(john.name); // logs "John"
     ```
4. **With call(), apply(), or bind() methods:** You can explicitly set the value of `this` using these methods.
   - Example:
     ```jsx
     function sayName() {
       console.log(this.name);
     }
     const obj = { name: "John" };
     sayName.call(obj); // logs "John"
     ```

**Memorable Tip:**

Think of `this` as a reference to the current object, and its value changes based on how the function is called.

## 35) What are all the types of Pop up boxes available in JavaScript?

**JavaScript Pop-up Boxes:**

JavaScript offers several types of pop-up boxes, also known as dialogs or modals, to display information or prompt user input. Here are the main types:

1. **Alert:** Displays important information or warnings. It has only an "OK" button.
   - Syntax: `alert(message);`
   - Example: `alert("Hello, World!");`
2. **Confirm:** Asks the user to confirm an action with "OK" and "Cancel" buttons. It returns a boolean value (`true` for "OK," `false` for "Cancel").
   - Syntax: `confirm(message);`
   - Example: `let isConfirmed = confirm("Are you sure?");`
3. **Prompt:** Asks the user for input with an "OK" and "Cancel" buttons. It returns the user's input as a string or `null` if the user clicks "Cancel."
   - Syntax: `prompt(message, [defaultValue]);`
   - Example: `let userInput = prompt("Enter your name:", "Guest");`
4. **Custom Modals:** Create custom pop-up boxes using HTML, CSS, and JavaScript. You can control their appearance, content, and behavior.
   - Example using Bootstrap's Modal component:
     ```html
     <!-- Modal -->
     <div
       class="modal fade"
       id="myModal"
       tabindex="-1"
       aria-labelledby="exampleModalLabel"
       aria-hidden="true"
     >
       <div class="modal-dialog">
         <div class="modal-content">
           <div class="modal-header">
             <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
             <button
               type="button"
               class="btn-close"
               data-bs-dismiss="modal"
               aria-label="Close"
             ></button>
           </div>
           <div class="modal-body">...</div>
           <div class="modal-footer">
             <button
               type="button"
               class="btn btn-secondary"
               data-bs-dismiss="modal"
             >
               Close
             </button>
             <button type="button" class="btn btn-primary">Save changes</button>
           </div>
         </div>
       </div>
     </div>
     ```
     ```jsx
     const myModal = new bootstrap.Modal(document.getElementById("myModal"));
     myModal.show();
     ```

These pop-up boxes can be used to provide feedback, ask for user input, or display important information. Custom modals offer more flexibility and control over the appearance and behavior of pop-up boxes.

## 36) How are DOM utilised in JavaScript?

**Utilizing the Document Object Model (DOM) in JavaScript:**

The Document Object Model (DOM) is a programming interface for web documents. It represents a page so that programs can change the document structure, style, and content. Here's how you can utilize the DOM in JavaScript:

1. **Accessing Elements:**
   - By ID: `document.getElementById('id')`
   - By Class Name: `document.getElementsByClassName('className')`
   - By Tag Name: `document.getElementsByTagName('tagName')`
   - By Selector (using querySelector or querySelectorAll): `document.querySelector('#id')`, `document.querySelectorAll('.className')`
2. **Creating Elements:**
   - Using `createElement()`: `let newElement = document.createElement('tagName');`
3. **Manipulating Content:**
   - Inner Text: `element.innerText = 'new text';`
   - Inner HTML: `element.innerHTML = '<new html content>';`
   - Text Content: `element.textContent = 'new text';`
4. **Changing Attributes:**
   - Getting an attribute: `let attrValue = element.getAttribute('attributeName');`
   - Setting an attribute: `element.setAttribute('attributeName', 'newValue');`
   - Removing an attribute: `element.removeAttribute('attributeName');`
5. **Modifying Styles:**
   - Inline styles: `element.style.property = 'value';`
   - ClassList: `element.classList.add('className');`, `element.classList.remove('className');`, `element.classList.toggle('className');`
   - Computed styles: `let style = window.getComputedStyle(element);`
6. **Event Handling:**
   - Adding an event listener: `element.addEventListener('eventType', function);`
7. **Traversing the DOM:**
   - Parent: `element.parentElement;`
   - Children: `element.children;`
   - Siblings: `element.previousElementSibling`, `element.nextElementSibling;`
   - First/Last Child: `element.firstElementChild`, `element.lastElementChild;`

Here's a simple example of accessing, manipulating, and event handling with the DOM:

```jsx
// Access an element by ID
const myElement = document.getElementById("myElement");

// Change the inner text
myElement.innerText = "New text content";

// Add an event listener
myElement.addEventListener("click", function () {
  alert("You clicked the element!");
});
```

Understanding and utilizing the DOM is crucial for working with web pages in JavaScript, enabling you to interact with, manipulate, and respond to HTML content dynamically.

## 37) How are event handlers utilised in JavaScript?

**Utilizing Event Handlers in JavaScript:**

Event handlers in JavaScript allow you to respond to user interactions and other events, such as mouse clicks, key presses, or page loading. Here's how you can utilize event handlers in a simple, memorable way:

1. **Adding Event Listeners:**
   - Using `addEventListener()` method:
     ```jsx
     element.addEventListener('eventType', function);

     ```
   - Example: Add a click event listener to a button:
     ```jsx
     const myButton = document.getElementById("myButton");
     myButton.addEventListener("click", function () {
       alert("Button clicked!");
     });
     ```
2. **Inline Event Handlers (not recommended):**
   - Attaching event handlers directly in HTML attributes:
     ```html
     <button onclick="myFunction()">Click me</button>
     ```
   - Example function:
     ```jsx
     function myFunction() {
       alert("Button clicked!");
     }
     ```
3. **Removing Event Listeners:**
   - Using `removeEventListener()` method:
     ```jsx
     element.removeEventListener('eventType', function);

     ```
   - Example: Remove the click event listener after a single click:
     ```jsx
     const myButton = document.getElementById('myButton');
     let clickCount = 0;
     myButton.addEventListener('click', function() {
       alert('Button clicked!');
       clickCount++;
       if (clickCount === 1) {
         myButton.removeEventListener('click', function);
       }
     });

     ```
4. **Event Object:**
   - The `event` object contains information about the event, like the target element, mouse position, or key code.
   - Example: Accessing the target element:
     ```jsx
     element.addEventListener("click", function (event) {
       console.log("Clicked element:", event.target);
     });
     ```
5. **Preventing Default Behavior:**
   - Using `event.preventDefault()` to stop the default behavior of an event.
   - Example: Preventing a link from following its URL:
     ```jsx
     const myLink = document.getElementById("myLink");
     myLink.addEventListener("click", function (event) {
       event.preventDefault();
       alert("Link clicked!");
     });
     ```
