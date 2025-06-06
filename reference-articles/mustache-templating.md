# Mustache Templating

The ComUnity Development Toolkit offers advanced templating capabilities that enhance dynamic data rendering and application interactivity. Within the Toolkit, application definitions are designed to support template values, streamlining the runtime binding of data and arguments.

**Template Syntax**

The standard format for a template is expressed as:

```
{{=<name>}}
```

At runtime, the template `{{=<name>}}` is seamlessly replaced with the corresponding data value for `name`. If the value is not available in the current context, the template reverts to an empty string.

**Fields Supporting Templated Values**

The fields in the Toolkit that typically support templated values are **Data Path** and **Target URLs**. These fields allow for dynamic referencing and navigation within the application, ensuring that data is always accurately presented and linked.

**Key Features**:

1.  **Templating in Markdown:** \


    ```markdown
    __Logged in as: {{=identifier}}__

    ```
2.  **Templated Parameters in OData Queries**:

    The Toolkit's support for templated parameters within[ OData 3.0](https://www.odata.org/documentation/odata-version-3-0/?msclkid=237b40adce7311ecae5bf187856e481c) queries enables developers to devise detailed queries tailored to the application's specific needs see [oData](odata.md) section for more details. This eradicates the constraints of using static values, granting developers the liberty to use dynamic placeholders for greater query adaptability.
3.  **Dynamic Data Navigation Between Screens:**

    Templating isn't limited to just data fetching. It also extends to inter-screen data navigation. By using templated URLs, developers can pass data between different screens in the application. For example, the following Target URL can be used to navigate to the `FaultEditPage` and pass the `faultId` value:

    ```
    LINK:FaultEditPage?faultId={{= FaultId }}
    ```

    In this scenario, the `{{= FaultId }}` placeholder gets substituted with the actual `FaultId` variable's value when the URL is triggered. This mechanism removes the necessity of hardcoded values, ensuring a more dynamic navigation experience.

### Templating Rules&#x20;

The following are the templating rules:

* The `{{= <name> }}` template is used to replace the placeholder `<name>` with the value of the property `name` in the JSON payload.
* The `{{= <object>/<property> }}` template is used to replace the placeholder `<property>` with the value of the property `property` in the object `<object>` in the JSON payload.
* The `.` and `/` characters are interchangeable in the templates, so they can be used interchangeably to access properties in the JSON payload.
*   There are also special tags:  &#x20;

    ```
    {{= userguid }} - The Id of the current user
    {{= now }} - Current time
    ```

    These tags can be used to access information that is not stored in the JSON payload, such as     the current user's Id or the current time.       &#x20;

**Example**

The following JSON payload is returned from the Data Service:

```json5
{
"name": "John",
"surname": "Doe",
"UserProfile": {
 "Suburb": "Rivonia",
 "Email": "jd@home.com"
 }
"Business": {
 "Name": "JD Take aways”,
 "BusinessType": {
 "Name": " Restaurants",
 "Description": "Places to eat"
                }
           }
}

```

The following table shows how each template is parsed during runtime:

| **Template**                        | **Parsed Value**           |
| ----------------------------------- | -------------------------- |
| `Hello {{= name }}, welcome back`   | `Hello John, welcome back` |
| `{{= UserProfile/Suburb }}`         | `Rivonia`                  |
| `{{= Business.BusinessType.Name }}` | `Restaurants`              |
| `Address: {{= Address }}`           | `Address:`                 |

### Contexts

There are two types of contexts in the ComUnity Development Toolkit:

* **User context:** This context is always available and contains the session values from the UserProfile table for the current user. The values can be accessed using the following templates:
  * `{{= profile/Cell }}`
  * `{{= profile.Name }}`
* **Page / Form context:** This context is unique and derived from a record and/or link argument values. The values can be accessed using the following templates:
  * `{{= linkArgName }}` - for a link argument (i.e. `recordId`)
  * `{{= FieldName }}` - for a specific field on a record (i.e. `Name`)

The user context is the most common context and is used to access the user's session values, such as their name, email address, and role. The page / form context is used to access the values of the arguments passed from parent links and the fields of the record that the page is referencing.
