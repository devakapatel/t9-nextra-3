# Unit 2

## <mark> 1) What is VIEW? Explain how to create and modify Views? </mark>

### View in Android

A **View** in Android is a **UI component** that is used to **display and interact with elements** in an application. Examples of Views include **Button, TextView, EditText, ImageView**, etc. All Views are subclasses of the `android.view.View` class.

### **Creating a View**

1. **Using XML (Recommended)**

   - Define a View in an XML layout file (`res/layout/activity_main.xml`).
   - Example:
     ```xml
     <TextView
         android:id="@+id/textView"
         android:layout_width="wrap_content"
         android:layout_height="wrap_content"
         android:text="Hello, Android!" />
     ```

2. **Using Java/Kotlin Code**
   - Create a View dynamically in the `MainActivity.java`.
   - Example (Java):
     ```java
     TextView textView = new TextView(this);
     textView.setText("Hello, Android!");
     textView.setLayoutParams(new LinearLayout.LayoutParams(
         LinearLayout.LayoutParams.WRAP_CONTENT,
         LinearLayout.LayoutParams.WRAP_CONTENT));
     ```

### **Modifying a View**

1. **Changing View Properties in Java**

   - Modify a View dynamically in code.
   - Example:
     ```java
     TextView textView = findViewById(R.id.textView);
     textView.setText("Updated Text");
     textView.setTextSize(20);
     textView.setTextColor(Color.RED);
     ```

2. **Handling User Interaction**
   - Set an **onClickListener** to respond to user actions.
   - Example:
     ```java
     Button button = findViewById(R.id.button);
     button.setOnClickListener(new View.OnClickListener() {
         @Override
         public void onClick(View v) {
             textView.setText("Button Clicked!");
         }
     });
     ```

### **Conclusion**

Views are **building blocks of UI design** in Android. They can be **created, modified, and interacted with** using XML or Java/Kotlin code to build interactive applications.

## <mark> 2) Explain the concept of Datepicker and Timepicker. </mark>

### DatePicker and TimePicker in Android

**DatePicker** and **TimePicker** are UI components in Android that allow users to **select a date or time** in an intuitive way.

### **1. DatePicker**

- Used to **select a date** (day, month, year).
- Can be displayed as:
  - **DatePickerDialog** (popup dialog).
  - **DatePicker Widget** (embedded in the layout).

#### **Example: DatePickerDialog in Java**

```java
// Open DatePickerDialog when button is clicked
Button btnSelectDate = findViewById(R.id.btnSelectDate);
btnSelectDate.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {
        Calendar calendar = Calendar.getInstance();
        int year = calendar.get(Calendar.YEAR);
        int month = calendar.get(Calendar.MONTH);
        int day = calendar.get(Calendar.DAY_OF_MONTH);

        DatePickerDialog datePickerDialog = new DatePickerDialog(MainActivity.this,
            (view, selectedYear, selectedMonth, selectedDay) -> {
                // Set selected date in TextView
                TextView dateTextView = findViewById(R.id.dateTextView);
                dateTextView.setText(selectedDay + "/" + (selectedMonth + 1) + "/" + selectedYear);
            }, year, month, day);

        datePickerDialog.show();
    }
});
```

### **2. TimePicker**

- Used to **select a time** (hour, minute).
- Can be displayed as:
  - **TimePickerDialog** (popup).
  - **TimePicker Widget** (in the layout).
- Supports **12-hour or 24-hour format**.

#### **Example: TimePickerDialog in Java**

```java
// Open TimePickerDialog when button is clicked
Button btnSelectTime = findViewById(R.id.btnSelectTime);
btnSelectTime.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {
        Calendar calendar = Calendar.getInstance();
        int hour = calendar.get(Calendar.HOUR_OF_DAY);
        int minute = calendar.get(Calendar.MINUTE);

        TimePickerDialog timePickerDialog = new TimePickerDialog(MainActivity.this,
            (view, selectedHour, selectedMinute) -> {
                // Set selected time in TextView
                TextView timeTextView = findViewById(R.id.timeTextView);
                timeTextView.setText(selectedHour + ":" + selectedMinute);
            }, hour, minute, true);

        timePickerDialog.show();
    }
});
```

### **Conclusion**

- **DatePicker** is used to select a date, while **TimePicker** is used to select a time.
- Both can be implemented using **dialogs or UI widgets**.
- These components improve **user experience** by providing a structured way to input dates and times.

## <mark> 3) Explain the term localization in Android with example. </mark>

### Localization in Android

**Localization** in Android refers to the process of **adapting an application for different languages, regions, and cultures**. It helps in making an app **accessible to a global audience** by providing text, images, and other resources in different languages.

### **Key Features of Localization**

1. **Supports Multiple Languages** – Users can view the app in their preferred language.
2. **Region-Specific Formatting** – Handles date, time, currency, and number formats.
3. **Uses Resource Files** – Stores text in `res/values/` folders to support different languages.

### **Steps for Implementing Localization**

1. **Define Default Strings in `res/values/strings.xml`**

   ```xml
   <resources>
       <string name="app_name">My Application</string>
       <string name="greeting">Hello, Welcome!</string>
   </resources>
   ```

2. **Create Language-Specific `strings.xml` Files**

   - **For French (`res/values-fr/strings.xml`)**
     ```xml
     <resources>
         <string name="app_name">Mon Application</string>
         <string name="greeting">Bonjour, Bienvenue!</string>
     </resources>
     ```
   - **For Spanish (`res/values-es/strings.xml`)**
     ```xml
     <resources>
         <string name="app_name">Mi Aplicación</string>
         <string name="greeting">Hola, ¡Bienvenido!</string>
     </resources>
     ```

3. **Android Automatically Detects User Language**

   - If the device language is **French**, Android loads `values-fr/strings.xml`.
   - If the language is **not supported**, the default `values/strings.xml` is used.

4. **Using Localized Strings in Code**
   ```java
   TextView textView = findViewById(R.id.textView);
   textView.setText(getString(R.string.greeting));
   ```

### **Conclusion**

Localization in Android allows apps to **adapt to different languages and regions**, improving user experience and **expanding the app’s global reach**.

## <mark> 4) Explain how to listen Native Broadcast Intents. </mark>

### Listening to Native Broadcast Intents in Android

**Broadcast Intents** are messages sent by the Android system or applications to notify components about specific events. **Native Broadcast Intents** are system-generated broadcasts (e.g., battery status, network changes).

To **listen to Native Broadcast Intents**, we use a **BroadcastReceiver**, which responds when the system sends a broadcast.

### **Steps to Listen to Native Broadcast Intents**

#### **1. Create a BroadcastReceiver Class**

Define a `BroadcastReceiver` that listens for system events.  
Example: Listening for **battery level changes**.

```java
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.widget.Toast;

public class BatteryReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        int level = intent.getIntExtra("level", -1); // Get battery level
        Toast.makeText(context, "Battery Level: " + level + "%", Toast.LENGTH_SHORT).show();
    }
}
```

#### **2. Register the Receiver in `AndroidManifest.xml`**

Add the receiver inside the `<application>` tag.

```xml
<receiver android:name=".BatteryReceiver">
    <intent-filter>
        <action android:name="android.intent.action.BATTERY_CHANGED"/>
    </intent-filter>
</receiver>
```

#### **3. Register Receiver Dynamically in Activity (Optional)**

Instead of declaring in `AndroidManifest.xml`, you can register it in an activity.

```java
BatteryReceiver batteryReceiver = new BatteryReceiver();

@Override
protected void onResume() {
    super.onResume();
    IntentFilter filter = new IntentFilter(Intent.ACTION_BATTERY_CHANGED);
    registerReceiver(batteryReceiver, filter);
}

@Override
protected void onPause() {
    super.onPause();
    unregisterReceiver(batteryReceiver);
}
```

### **Common Native Broadcast Intents**

| Intent Action                              | Description                     |
| ------------------------------------------ | ------------------------------- |
| `android.intent.action.BATTERY_CHANGED`    | Battery level or state change.  |
| `android.net.conn.CONNECTIVITY_CHANGE`     | Network connectivity change.    |
| `android.intent.action.AIRPLANE_MODE`      | Airplane mode enabled/disabled. |
| `android.intent.action.POWER_CONNECTED`    | Device connected to power.      |
| `android.intent.action.POWER_DISCONNECTED` | Device disconnected from power. |

### **Conclusion**

Listening to **Native Broadcast Intents** allows apps to respond to system events like **battery status, network changes, and power connections**, improving app functionality and user experience.

## <mark> 5) Explain the concept of Download Manager. </mark>

### Download Manager in Android

**Download Manager** is an Android system service that **handles long-running downloads in the background**. It allows applications to download files efficiently while handling **network failures, system reboots, and retries** automatically.

### **Features of Download Manager**

1. **Handles Large File Downloads** – Efficiently downloads large files without freezing the UI.
2. **Supports Background Downloading** – Runs downloads in the background, allowing users to continue using the app.
3. **Automatic Retry & Resume** – Resumes interrupted downloads due to network failures or system reboots.
4. **Manages Download Notifications** – Shows progress in the notification bar.
5. **Supports Various Network Conditions** – Can restrict downloads to Wi-Fi only.

### **Using Download Manager in Android**

#### **1. Add Permission in `AndroidManifest.xml`**

```xml
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
```

#### **2. Start a File Download**

```java
import android.app.DownloadManager;
import android.content.Context;
import android.net.Uri;
import android.os.Environment;

public void startDownload(Context context) {
    DownloadManager downloadManager = (DownloadManager) context.getSystemService(Context.DOWNLOAD_SERVICE);

    Uri uri = Uri.parse("https://example.com/sample.pdf"); // File URL

    DownloadManager.Request request = new DownloadManager.Request(uri);
    request.setTitle("Downloading File");
    request.setDescription("Downloading sample.pdf");
    request.setDestinationInExternalPublicDir(Environment.DIRECTORY_DOWNLOADS, "sample.pdf");
    request.setNotificationVisibility(DownloadManager.Request.VISIBILITY_VISIBLE_NOTIFY_COMPLETED);

    if (downloadManager != null) {
        downloadManager.enqueue(request);
    }
}
```

### **3. Monitor Download Progress**

To track download status, register a `BroadcastReceiver`.

```java
import android.app.DownloadManager;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.widget.Toast;

public class DownloadReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        long downloadId = intent.getLongExtra(DownloadManager.EXTRA_DOWNLOAD_ID, -1);
        Toast.makeText(context, "Download Completed! ID: " + downloadId, Toast.LENGTH_SHORT).show();
    }
}
```

Register the receiver dynamically in an activity:

```java
registerReceiver(new DownloadReceiver(), new IntentFilter(DownloadManager.ACTION_DOWNLOAD_COMPLETE));
```

### **Use Cases of Download Manager**

- **Downloading PDFs, images, or videos** in apps.
- **Updating files in the background** for offline access.
- **Handling large downloads** without affecting app performance.

### **Conclusion**

Download Manager simplifies downloading large files by handling **background tasks, failures, and progress tracking**, ensuring a **smooth user experience**.

## <mark> 6) Explain Types of Menu Available in Android. </mark>

### Types of Menu in Android

Android provides **three types of menus** to display options and actions in an application. These menus help improve **user interaction and navigation**.

### **1. Options Menu**

- The **primary menu** for an activity, displayed in the **toolbar/action bar**.
- Typically used for **settings, search, or common actions**.
- Appears when the user taps the **three-dot menu**.

#### **Example: Creating an Options Menu**

**Step 1: Define Menu in XML (`res/menu/menu_main.xml`)**

```xml
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:id="@+id/action_settings"
        android:title="Settings"
        android:showAsAction="never"/>
    <item android:id="@+id/action_search"
        android:title="Search"
        android:showAsAction="ifRoom"/>
</menu>
```

**Step 2: Load Menu in Activity (`MainActivity.java`)**

```java
@Override
public boolean onCreateOptionsMenu(Menu menu) {
    getMenuInflater().inflate(R.menu.menu_main, menu);
    return true;
}
```

### **2. Context Menu**

- A **floating menu** that appears **on long press** of a UI element.
- Used for **actions related to a specific item**, like **edit, delete, or share**.

#### **Example: Creating a Context Menu**

**Step 1: Register View for Context Menu (`MainActivity.java`)**

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);

    TextView textView = findViewById(R.id.textView);
    registerForContextMenu(textView);
}
```

**Step 2: Create Context Menu (`MainActivity.java`)**

```java
@Override
public void onCreateContextMenu(ContextMenu menu, View v, ContextMenu.ContextMenuInfo menuInfo) {
    super.onCreateContextMenu(menu, v, menuInfo);
    menu.setHeaderTitle("Select Action");
    menu.add(0, v.getId(), 0, "Edit");
    menu.add(0, v.getId(), 0, "Delete");
}
```

### **3. Popup Menu**

- A **temporary menu** that appears **next to a clicked view**.
- Used for **quick actions like selecting an item or sharing content**.

#### **Example: Creating a Popup Menu**

**Step 1: Create Popup Menu in Java (`MainActivity.java`)**

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);

    Button button = findViewById(R.id.button);
    button.setOnClickListener(v -> {
        PopupMenu popup = new PopupMenu(MainActivity.this, v);
        popup.getMenuInflater().inflate(R.menu.menu_popup, popup.getMenu());
        popup.show();
    });
}
```

**Step 2: Define Menu Items (`res/menu/menu_popup.xml`)**

```xml
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:id="@+id/action_share"
        android:title="Share"/>
    <item android:id="@+id/action_favorite"
        android:title="Add to Favorites"/>
</menu>
```

### **Comparison of Menus**

| Menu Type        | How It Appears                  | Use Case                                       |
| ---------------- | ------------------------------- | ---------------------------------------------- |
| **Options Menu** | In the toolbar (three-dot menu) | App-wide actions like **Settings, Search**     |
| **Context Menu** | On long press of an item        | Item-specific actions like **Edit, Delete**    |
| **Popup Menu**   | Next to a clicked view          | Quick actions like **Share, Add to Favorites** |

### **Conclusion**

Android menus enhance **user experience** by providing structured ways to **navigate, interact, and perform actions** within an app.

## <mark> 7) Explain spinner in detail with pseudo code. </mark>

### Spinner in Android

A **Spinner** in Android is a **dropdown UI component** that allows users to **select one option from a list**. It is similar to a dropdown menu in web development.

### **Features of Spinner**

1. **Dropdown List** – Displays a list of selectable items.
2. **Default Selection** – Shows the first item by default.
3. **Customizable Appearance** – Can be styled using custom adapters.
4. **Efficient UI Component** – Saves space compared to RadioButtons.

### **Steps to Implement a Spinner**

#### **1. Define Spinner in XML Layout** (`res/layout/activity_main.xml`)

```xml
<Spinner
    android:id="@+id/spinner"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"/>
```

#### **2. Create and Set Data in Java** (`MainActivity.java`)

```java
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Step 1: Initialize Spinner
        Spinner mySpinner = findViewById(R.id.spinner);

        // Step 2: Define data for Spinner (Dropdown items)
        String[] items = {"Option 1", "Option 2", "Option 3", "Option 4"};

        // Step 3: Create an ArrayAdapter to link data with Spinner
        ArrayAdapter<String> adapter = new ArrayAdapter<>(
            this,
            android.R.layout.simple_spinner_item,
            items
        );
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

        // Step 4: Set Adapter to Spinner
        mySpinner.setAdapter(adapter);

        // Step 5: Handle item selection from Spinner
        mySpinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                String selectedItem = parent.getItemAtPosition(position).toString();
                Toast.makeText(MainActivity.this, "Selected: " + selectedItem, Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {
                // Do nothing if no item is selected
            }
        });
    }
}
```

### **Explanation**

1. **Define Spinner in XML** – Adds a Spinner component to the UI.
2. **Create Data Source** – Defines a list of selectable options.
3. **Use an ArrayAdapter** – Binds the list to the Spinner.
4. **Set the Adapter** – Attaches the adapter to the Spinner.
5. **Handle Selection Events** – Uses `setOnItemSelectedListener()` to capture user selection.

### **Conclusion**

A **Spinner** is a user-friendly dropdown component that allows users to **select one item from a list**. It improves UI efficiency and is commonly used for **form inputs, filters, and settings menus**.

## <mark> 8) Write down the pseudo code for Radio button and Checkbox. </mark>

### **Pseudo Code for RadioButton and CheckBox in Android**

### **1. RadioButton in Android**

A **RadioButton** allows users to **select only one option** from a group.

#### **XML Layout for RadioButton (`activity_main.xml`)**

```xml
<RadioGroup
    android:id="@+id/radioGroup"
    android:layout_width="match_parent"
    android:layout_height="wrap_content">

    <RadioButton
        android:id="@+id/radioButton1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Option 1" />

    <RadioButton
        android:id="@+id/radioButton2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Option 2" />
</RadioGroup>

<Button
    android:id="@+id/submitButton"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Submit"/>
```

#### **Java Code for RadioButton (`MainActivity.java`)**

```java
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize RadioGroup and Button
        RadioGroup radioGroup = findViewById(R.id.radioGroup);
        Button submitButton = findViewById(R.id.submitButton);

        // Handle Button Click
        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int selectedId = radioGroup.getCheckedRadioButtonId();
                if (selectedId != -1) {
                    RadioButton selectedRadioButton = findViewById(selectedId);
                    Toast.makeText(MainActivity.this, "Selected: " + selectedRadioButton.getText(), Toast.LENGTH_SHORT).show();
                } else {
                    Toast.makeText(MainActivity.this, "No selection made", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}
```

### **2. CheckBox in Android**

A **CheckBox** allows users to **select multiple options** independently.

#### **XML Layout for CheckBox (`activity_main.xml`)**

```xml
<CheckBox
    android:id="@+id/checkBox1"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Option 1"/>

<CheckBox
    android:id="@+id/checkBox2"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Option 2"/>

<Button
    android:id="@+id/submitButton"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Submit"/>
```

#### **Java Code for CheckBox (`MainActivity.java`)**

```java
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize CheckBoxes and Button
        CheckBox checkBox1 = findViewById(R.id.checkBox1);
        CheckBox checkBox2 = findViewById(R.id.checkBox2);
        Button submitButton = findViewById(R.id.submitButton);

        // Handle Button Click
        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                StringBuilder result = new StringBuilder("Selected: ");
                if (checkBox1.isChecked()) {
                    result.append(checkBox1.getText()).append(" ");
                }
                if (checkBox2.isChecked()) {
                    result.append(checkBox2.getText()).append(" ");
                }
                if (result.toString().equals("Selected: ")) {
                    result.append("None");
                }
                Toast.makeText(MainActivity.this, result.toString(), Toast.LENGTH_SHORT).show();
            }
        });
    }
}
```

### **Conclusion**

- **RadioButton** allows **only one selection** from a group.
- **CheckBox** allows **multiple selections** independently.
- Both can be used to capture user preferences in Android apps.

## <mark> 9) Explain Checkbox in Android with example. </mark>

### CheckBox in Android

A **CheckBox** in Android is a **UI component** that allows users to **select multiple options independently**. It is useful for cases where users may choose **more than one option**, such as selecting preferences, settings, or features.

### **Features of CheckBox**

1. **Multiple Selection** – Users can select **one or more** options.
2. **Independent State** – Each checkbox operates separately.
3. **Two-State Behavior** – A checkbox can be **checked (true)** or **unchecked (false)**.
4. **Custom Styling** – Checkboxes can be styled with custom colors and images.

### **Example: Implementing CheckBox in Android**

#### **1. Define CheckBoxes in XML (`activity_main.xml`)**

```xml
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <CheckBox
        android:id="@+id/checkBox1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Option 1" />

    <CheckBox
        android:id="@+id/checkBox2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Option 2" />

    <Button
        android:id="@+id/submitButton"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Submit"/>
</LinearLayout>
```

#### **2. Handle CheckBox Selection in Java (`MainActivity.java`)**

```java
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize CheckBoxes and Button
        CheckBox checkBox1 = findViewById(R.id.checkBox1);
        CheckBox checkBox2 = findViewById(R.id.checkBox2);
        Button submitButton = findViewById(R.id.submitButton);

        // Handle Button Click
        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                StringBuilder result = new StringBuilder("Selected: ");
                if (checkBox1.isChecked()) {
                    result.append(checkBox1.getText()).append(" ");
                }
                if (checkBox2.isChecked()) {
                    result.append(checkBox2.getText()).append(" ");
                }
                if (result.toString().equals("Selected: ")) {
                    result.append("None");
                }
                Toast.makeText(MainActivity.this, result.toString(), Toast.LENGTH_SHORT).show();
            }
        });
    }
}
```

### **Explanation**

1. **CheckBoxes are defined in XML** – Users can select multiple options.
2. **Initialize CheckBoxes in Java** – Retrieve their state using `isChecked()`.
3. **Handle Button Click** – Display selected options using `Toast`.

### **Use Cases of CheckBox**

- Selecting **multiple interests/preferences** (e.g., "Sports", "Music", "Movies").
- Enabling/disabling **features** in an app (e.g., "Enable Notifications", "Dark Mode").
- Accepting **terms and conditions** before proceeding.

### **Conclusion**

A **CheckBox** in Android provides an easy way to **select multiple options**. It enhances user interaction by allowing **customizable selections** in forms, settings, and preference screens.

## <mark> 10) Explain Edit text in Android with example. </mark>

### EditText in Android

**EditText** is an Android UI component that allows users to **input text** in an application. It is commonly used for **forms, login screens, and user feedback sections**.

### **Features of EditText**

1. **User Input** – Allows users to type text.
2. **Customizable Input Type** – Supports text, numbers, passwords, email, etc.
3. **Hint Text** – Displays a placeholder inside the text field.
4. **Validation Support** – Can restrict input length and format.
5. **Auto-Correction & Suggestions** – Supports predictive text.

### **Example: Implementing EditText in Android**

#### **1. Define EditText in XML (`activity_main.xml`)**

```xml
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <EditText
        android:id="@+id/editTextName"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter your name"
        android:inputType="textPersonName" />

    <Button
        android:id="@+id/submitButton"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Submit"/>
</LinearLayout>
```

#### **2. Handle EditText Input in Java (`MainActivity.java`)**

```java
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize EditText and Button
        EditText editTextName = findViewById(R.id.editTextName);
        Button submitButton = findViewById(R.id.submitButton);

        // Handle Button Click
        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String name = editTextName.getText().toString().trim();
                if (!name.isEmpty()) {
                    Toast.makeText(MainActivity.this, "Hello, " + name + "!", Toast.LENGTH_SHORT).show();
                } else {
                    Toast.makeText(MainActivity.this, "Please enter your name", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}
```

### **Explanation**

1. **EditText in XML** – Accepts user input with a placeholder (`hint`).
2. **Retrieve Text in Java** – `editText.getText().toString()` gets the input.
3. **Validate Input** – Ensures the field is not empty before showing a message.
4. **Display Input Using Toast** – Shows a greeting message with the entered name.

### **Common Input Types in EditText**

| Input Type         | Description                        |
| ------------------ | ---------------------------------- |
| `textPersonName`   | Name input                         |
| `textEmailAddress` | Email input                        |
| `phone`            | Phone number input                 |
| `number`           | Numeric input                      |
| `textPassword`     | Password input (hidden characters) |

### **Use Cases of EditText**

- **Login and Registration Forms** – Accept usernames, passwords, and emails.
- **Search Fields** – Allow users to search content in an app.
- **Feedback Forms** – Collect user comments and reviews.

### **Conclusion**

EditText is a key UI component for **user input** in Android apps. It supports **different input types, validation, and customization**, making it suitable for various applications.

## <mark> 11) Explain Text view in Android with example. </mark>

### TextView in Android

**TextView** is a UI component in Android used to **display static or dynamic text** on the screen. It does not allow user input like `EditText` but is commonly used for labels, headings, and displaying messages.

### **Features of TextView**

1. **Displays Read-Only Text** – Used for labels, descriptions, and instructions.
2. **Supports Styling** – Can change **font size, color, style, and alignment**.
3. **Dynamic Text Update** – Can update text programmatically.
4. **Supports Click Events** – Can detect clicks using `setOnClickListener()`.

### **Example: Implementing TextView in Android**

#### **1. Define TextView in XML (`activity_main.xml`)**

```xml
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <TextView
        android:id="@+id/textViewMessage"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello, Android!"
        android:textSize="20sp"
        android:textColor="#000000"
        android:padding="10dp" />

    <Button
        android:id="@+id/buttonChangeText"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Change Text"/>
</LinearLayout>
```

#### **2. Modify TextView Programmatically (`MainActivity.java`)**

```java
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize TextView and Button
        TextView textViewMessage = findViewById(R.id.textViewMessage);
        Button buttonChangeText = findViewById(R.id.buttonChangeText);

        // Handle Button Click to Change TextView Content
        buttonChangeText.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                textViewMessage.setText("Text Updated!");
            }
        });
    }
}
```

### **Explanation**

1. **TextView in XML** – Displays **default text**, styled with **size, color, and padding**.
2. **Modify Text in Java** – `textView.setText("New Text")` updates the displayed text.
3. **Button Click Listener** – Changes text dynamically when the button is clicked.

### **Common Properties of TextView**

| Property            | Description                                |
| ------------------- | ------------------------------------------ |
| `android:text`      | Sets the default text.                     |
| `android:textSize`  | Defines text size (e.g., `16sp`).          |
| `android:textColor` | Sets text color (e.g., `#FF0000` for red). |
| `android:textStyle` | Makes text **bold, italic, or normal**.    |
| `android:gravity`   | Aligns text **left, center, or right**.    |

### **Use Cases of TextView**

- Displaying **headings, labels, and instructions**.
- Showing **messages and notifications**.
- Updating **dynamic content** (e.g., **score in a game**).

### **Conclusion**

TextView is an essential UI element in Android for **displaying text**. It can be **styled, modified, and updated dynamically**, making it useful for **static and dynamic text content**.

## <mark> 12) Explain padding in Android with example. </mark>

### Padding in Android

**Padding** in Android is the **space between the content of a View and its border**. It defines how much **inner spacing** should be kept inside the View before the content starts.

### **Key Features of Padding**

1. **Creates Inner Spacing** – Prevents text or images from touching the edges of the View.
2. **Improves Readability** – Helps in better UI alignment and appearance.
3. **Can Be Applied Individually** – Supports padding for **top, bottom, left, and right** separately.
4. **Works with All Views** – Can be applied to **TextView, Button, ImageView, etc.**

### **Types of Padding in Android**

1. **`android:padding`** – Applies equal padding to all sides.
2. **`android:paddingLeft`**, `android:paddingRight` – Sets padding for left and right.
3. **`android:paddingTop`**, `android:paddingBottom` – Sets padding for top and bottom.
4. **`android:paddingHorizontal`**, `android:paddingVertical` _(API 26+)_ – Applies padding to left-right or top-bottom together.

### **Example: Using Padding in Android**

#### **1. Define Padding in XML (`activity_main.xml`)**

```xml
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <TextView
        android:id="@+id/textViewExample"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello, Android!"
        android:textSize="18sp"
        android:background="#CCCCCC"
        android:padding="20dp"/>

    <Button
        android:id="@+id/buttonExample"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Click Me"
        android:paddingHorizontal="10dp"
        android:paddingVertical="5dp"/>
</LinearLayout>
```

### **2. Modify Padding Programmatically (`MainActivity.java`)**

```java
import android.os.Bundle;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Access TextView and set padding dynamically
        TextView textView = findViewById(R.id.textViewExample);
        textView.setPadding(30, 10, 30, 10); // Left, Top, Right, Bottom (in pixels)
    }
}
```

### **Explanation**

1. **Padding in XML** – `android:padding="20dp"` adds equal spacing inside the `TextView`.
2. **Custom Padding for Buttons** – `android:paddingHorizontal="10dp"` sets horizontal padding only.
3. **Dynamic Padding in Java** – `setPadding(30, 10, 30, 10)` changes padding at runtime.

### **Difference Between Padding and Margin**

| Feature           | Padding                                                | Margin                                                                     |
| ----------------- | ------------------------------------------------------ | -------------------------------------------------------------------------- |
| **Definition**    | Space **inside** the View, between content and border. | Space **outside** the View, between the View and its parent/sibling Views. |
| **Affects Size?** | Increases View size by pushing content inward.         | Creates spacing without affecting View size.                               |
| **Usage**         | Used for text/image spacing inside a View.             | Used for layout spacing between Views.                                     |

### **Use Cases of Padding**

- **Improving UI Design** – Adds space to make UI elements readable.
- **Button & Text Spacing** – Ensures text doesn’t touch button edges.
- **Card & Image Layouts** – Provides uniform padding inside cards or images.

### **Conclusion**

Padding in Android **improves UI appearance** by creating **inner spacing** inside Views. It helps in **better alignment, readability, and visual appeal** of UI elements.

## <mark> 13) Explain Button and types of buttons in android. </mark>

### Button in Android

A **Button** in Android is a **UI component** that allows users to **perform an action** when clicked. It is commonly used for **submitting forms, navigating between activities, or triggering events**.

### **Types of Buttons in Android**

#### **1. Normal Button (`Button`)**

- The default button used for general actions.
- Example:
  ```xml
  <Button
      android:id="@+id/buttonSubmit"
      android:layout_width="wrap_content"
      android:layout_height="wrap_content"
      android:text="Submit" />
  ```

#### **2. Image Button (`ImageButton`)**

- A button that displays an **image** instead of text.
- Example:
  ```xml
  <ImageButton
      android:id="@+id/imageButton"
      android:layout_width="wrap_content"
      android:layout_height="wrap_content"
      android:src="@drawable/ic_launcher" />
  ```

#### **3. Toggle Button (`ToggleButton`)**

- A button that switches **between ON and OFF states**.
- Example:
  ```xml
  <ToggleButton
      android:id="@+id/toggleButton"
      android:layout_width="wrap_content"
      android:layout_height="wrap_content"
      android:textOn="ON"
      android:textOff="OFF" />
  ```

#### **4. Radio Button (`RadioButton`)**

- Allows users to **select one option from a group**.
- Example:
  ```xml
  <RadioGroup android:layout_width="match_parent" android:layout_height="wrap_content">
      <RadioButton android:id="@+id/radio1" android:text="Option 1"/>
      <RadioButton android:id="@+id/radio2" android:text="Option 2"/>
  </RadioGroup>
  ```

#### **5. CheckBox Button (`CheckBox`)**

- Allows **multiple selections**.
- Example:
  ```xml
  <CheckBox
      android:id="@+id/checkBox1"
      android:layout_width="wrap_content"
      android:layout_height="wrap_content"
      android:text="Accept Terms" />
  ```

#### **6. Floating Action Button (`FloatingActionButton`)**

- A **round button** that floats above the UI, typically for quick actions.
- Example:
  ```xml
  <com.google.android.material.floatingactionbutton.FloatingActionButton
      android:id="@+id/fab"
      android:layout_width="wrap_content"
      android:layout_height="wrap_content"
      android:src="@drawable/ic_add"/>
  ```

### **Example: Handling Button Click in Java (`MainActivity.java`)**

```java
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize Button
        Button buttonSubmit = findViewById(R.id.buttonSubmit);

        // Handle Button Click
        buttonSubmit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(MainActivity.this, "Button Clicked!", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
```

### **Conclusion**

Android provides different types of buttons for **various user interactions**, such as **normal buttons, image buttons, toggle buttons, and floating action buttons**. Buttons improve **user experience and navigation** within an app.

## <mark> 14) Define the role of XML, JAVA, Manifest and String files in android. </mark>

### **Role of XML, Java, Manifest, and String Files in Android**

Android applications are built using **multiple components**, including **XML for UI design**, **Java (or Kotlin) for logic**, **Manifest for app configuration**, and **String files for localization**.

### **1. XML Files (Extensible Markup Language)**

- Used for **defining UI layouts, resources, and configurations**.
- Located in the **`res/` directory**.

#### **Types of XML Files in Android**

| XML File                       | Purpose                               |
| ------------------------------ | ------------------------------------- |
| `res/layout/activity_main.xml` | Defines the UI layout of an activity. |
| `res/drawable/`                | Stores images and shape resources.    |
| `res/menu/`                    | Defines menu items for the app.       |
| `res/values/colors.xml`        | Stores app color definitions.         |

#### **Example (activity_main.xml)**

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <TextView
        android:text="Hello, Android!"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"/>
</LinearLayout>
```

### **2. Java Files**

- Contain the **application logic, event handling, and backend code**.
- Located in the **`src/main/java/com.example.myapp/` directory**.

#### **Example (MainActivity.java)**

```java
import android.os.Bundle;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        TextView textView = findViewById(R.id.textView);
        textView.setText("Welcome to Android!");
    }
}
```

### **3. Android Manifest File (`AndroidManifest.xml`)**

- **Registers components (Activities, Services, Broadcast Receivers)**.
- Declares **permissions** (e.g., Internet, Camera, Storage).
- Specifies **app metadata** (package name, theme, launcher activity).
- Located in the **`app/src/main/` directory**.

#### **Example (`AndroidManifest.xml`)**

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.myapp">

    <uses-permission android:name="android.permission.INTERNET"/>

    <application
        android:allowBackup="true"
        android:theme="@style/Theme.MyApp">

        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>

    </application>
</manifest>
```

### **4. String Resource File (`res/values/strings.xml`)**

- Stores **text values** separately to support **localization**.
- Avoids hardcoding text in Java/XML files.

#### **Example (`strings.xml`)**

```xml
<resources>
    <string name="app_name">My Application</string>
    <string name="welcome_message">Welcome to Android!</string>
</resources>
```

**Using in XML:**

```xml
<TextView android:text="@string/welcome_message"/>
```

**Using in Java:**

```java
textView.setText(getString(R.string.welcome_message));
```

### **Conclusion**

| Component                | Purpose                                                             |
| ------------------------ | ------------------------------------------------------------------- |
| **XML Files**            | Define UI structure, styles, colors, and menus.                     |
| **Java Files**           | Handle app logic, user interactions, and functionality.             |
| **Manifest File**        | Configures the app, declares permissions, and registers components. |
| **String Resource File** | Stores text separately for localization and easy management.        |

Each component plays a **crucial role** in Android development, ensuring **structured, maintainable, and scalable applications**.

## <mark> 15) Explain the term material design in android with an example. </mark>

### **Material Design in Android**

**Material Design** is a **design language** developed by **Google** to create modern, visually appealing, and user-friendly Android applications. It provides a **consistent UI experience** across different devices using **animations, shadows, depth effects, and responsive layouts**.

### **Key Features of Material Design**

1. **Elevation & Shadows** – Adds **depth and layering** to UI elements.
2. **Smooth Animations** – Uses **motion effects** for transitions.
3. **Bold Colors & Typography** – Promotes **clear and readable text**.
4. **Responsive UI** – Adapts layouts for different **screen sizes**.
5. **Material Components** – Provides **pre-built widgets** like **FloatingActionButton, CardView, AppBar, Bottom Navigation**.

### **Example: Implementing Material Design in Android**

#### **1. Add Material Design Dependencies (`build.gradle`)**

```gradle
dependencies {
    implementation 'com.google.android.material:material:1.9.0'
}
```

#### **2. Use Material Design Components in XML (`activity_main.xml`)**

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <!-- Material Design Button -->
    <com.google.android.material.button.MaterialButton
        android:id="@+id/materialButton"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Material Button"
        style="@style/Widget.MaterialComponents.Button.UnelevatedButton"/>

    <!-- Floating Action Button -->
    <com.google.android.material.floatingactionbutton.FloatingActionButton
        android:id="@+id/fab"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:src="@drawable/ic_add"
        app:backgroundTint="@color/purple_500"/>

    <!-- Material CardView -->
    <com.google.android.material.card.MaterialCardView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        app:cardCornerRadius="8dp"
        app:cardElevation="6dp"
        android:padding="16dp"
        android:layout_marginTop="16dp">

        <TextView
            android:text="This is a Material CardView"
            android:textSize="16sp"/>

    </com.google.android.material.card.MaterialCardView>

</LinearLayout>
```

#### **3. Handle Button Clicks in Java (`MainActivity.java`)**

```java
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import com.google.android.material.button.MaterialButton;
import com.google.android.material.floatingactionbutton.FloatingActionButton;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        MaterialButton materialButton = findViewById(R.id.materialButton);
        FloatingActionButton fab = findViewById(R.id.fab);

        materialButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(MainActivity.this, "Material Button Clicked", Toast.LENGTH_SHORT).show();
            }
        });

        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(MainActivity.this, "FAB Clicked", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
```

### **Conclusion**

**Material Design** improves **user experience** by adding **depth, motion, and responsive UI components**. Android provides **Material Components** like **MaterialButton, FloatingActionButton, and CardView**, which help in building **modern and attractive apps**.

## <mark> 16) Differentiate between android themes and style. </mark>

### **Difference Between Android Themes and Styles**

| Feature           | **Style**                                                                                                        | **Theme**                                                                                           |
| ----------------- | ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Definition**    | A **Style** is a set of **attributes** that define the appearance of a single **View** (Button, TextView, etc.). | A **Theme** is a collection of styles that apply **globally** to an entire Activity or Application. |
| **Scope**         | Applied to **individual UI components** (e.g., Button, TextView).                                                | Applied to **Activities or the entire app**.                                                        |
| **Usage**         | Defines **colors, text size, padding, margins**, etc., for a specific View.                                      | Controls **UI appearance**, such as **AppBar, Status Bar, Backgrounds, and Fonts** across the app.  |
| **Defined In**    | `res/values/styles.xml`                                                                                          | `res/values/themes.xml` or `styles.xml`                                                             |
| **Applied Using** | `style="@style/MyStyle"` in XML for a specific View.                                                             | `android:theme="@style/MyTheme"` in `AndroidManifest.xml` for the whole Activity or app.            |

### **Example of Style (Applied to a Single View)**

**styles.xml**

```xml
<resources>
    <style name="CustomButton">
        <item name="android:background">#6200EE</item>
        <item name="android:textColor">#FFFFFF</item>
        <item name="android:textSize">18sp</item>
        <item name="android:padding">10dp</item>
    </style>
</resources>
```

**Usage in XML Layout** (`activity_main.xml`)

```xml
<Button
    android:text="Styled Button"
    style="@style/CustomButton"/>
```

### **Example of Theme (Applied to Entire App or Activity)**

**themes.xml**

```xml
<resources xmlns:tools="http://schemas.android.com/tools">
    <style name="Theme.MyApp" parent="Theme.MaterialComponents.Light">
        <item name="colorPrimary">#6200EE</item>
        <item name="colorPrimaryVariant">#3700B3</item>
        <item name="colorAccent">#03DAC5</item>
    </style>
</resources>
```

**Apply in `AndroidManifest.xml`**

```xml
<application
    android:theme="@style/Theme.MyApp">
</application>
```

### **Conclusion**

- **Styles** define **individual View properties**, making UI elements **consistent**.
- **Themes** apply **styles globally**, ensuring **uniformity** across **Activities and the entire app**.

Both **styles and themes** enhance **UI consistency, flexibility, and maintainability** in Android development.
