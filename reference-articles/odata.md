---
description: >-
  The OData (Open Data Protocol) is a set of best practices for developing and
  using RESTful APIs.
---

# OData

The [ OData 3.0](https://www.odata.org/documentation/odata-version-3-0/?msclkid=237b40adce7311ecae5bf187856e481c) specification is a powerful way to fetch and display data from a Data service. This specification defines a standard way of exchanging data between systems, allowing developers to retrieve data from external sources such as a database or API. By utilising the capabilities of the oData 3.0 specification, developers can create dynamic and customisable lists that can be updated in real-time with minimal manual intervention.

An [OData URL](https://www.odata.org/documentation/odata-version-3-0/url-conventions/) consists of three parameters: the service root URL, resource path and query options.&#x20;

In the ComUnity Development Toolkit the service root URL is system defined and and is not exposed publicly for security reasons.&#x20;

{% hint style="warning" %}
The ComUnity Development Toolkit only supports the[ OData 3.0](https://www.odata.org/documentation/odata-version-3-0/?msclkid=237b40adce7311ecae5bf187856e481c) specification.&#x20;
{% endhint %}

The following links will provide you with more information on OData.

* [https://www.odata.org/](https://www.odata.org/)
* [https://hevodata.com/learn/odata-vs-rest/#u2](https://hevodata.com/learn/odata-vs-rest/#u2)
* [https://docs.microsoft.com/en-us/sql/integration-services/data-flow/odata-source?view=sql-server-ver15](https://docs.microsoft.com/en-us/sql/integration-services/data-flow/odata-source?view=sql-server-ver15)
* [https://www.odata.org/documentation/odata-version-3-0/url-conventions/](https://www.odata.org/documentation/odata-version-3-0/url-conventions/)
* [https://www.odata.org/odata-services/](https://www.odata.org/odata-services/)

### OData in 6 steps

The OData metadata enables the development of powerful generic client tools. The following six steps demonstrate interesting scenarios of OData across different programming platforms.

_Source: www.odata.org_

The link below will provide you with a better understanding of OData.

* [https://www.odata.org/getting-started/understand-odata-in-6-steps/](https://www.odata.org/getting-started/understand-odata-in-6-steps/)
* [https://docs.microsoft.com/en-us/odata/](https://docs.microsoft.com/en-us/odata/)

### How is OData used in the Toolkit

{% hint style="success" %}
This article describes in some detail how OData is used within the ComUnity Platform Toolkit.
{% endhint %}

The OData protocol and URL conventions are used to interact with the platform _Screen Controls_ in the following ways:&#x20;

* Specifying the target URL for buttons and links, the data path for the content of links or the data path for the reference values of a reference field.
* Populating a list with database values (the Data Path and any Query values).
* Getting record values for a form (the Target URL).

### Screen Controls in the Application Pages

<table><thead><tr><th width="159.2195700044924">App Action</th><th width="243.51567367143144">Field</th><th>OData Syntax</th></tr></thead><tbody><tr><td><strong>ActionButton</strong></td><td>UrlTemplate <br><em>(OData resource path)</em></td><td><em><code>/UserProfile(guid'{{=userguid}}')/Posts({{= postId }})</code></em></td></tr><tr><td></td><td>DocumentTemplate <br><em>(OData body)</em><br><br><em><mark style="color:red;">SME Note:</mark></em><mark style="color:red;"> DocTemplate control deprecated, should be replaced with a Content control</mark></td><td><em><code>{"NewsId":{{= NewsId }},"Deleted":"{{= now }}"}  OR</code></em>  <br><em><code>{"odata.type": "Demo211026.PersonalNotification","Message": "{{= Message }}", "Subject": "{{= Subject }}", "ClickAction": "{{= ClickAction }}"}</code></em></td></tr><tr><td><strong>BlockTemplate</strong></td><td>BlockUrl <br><em>(OData resource path)</em></td><td><em><mark style="color:red;"><strong>SME Note:</strong></mark><mark style="color:red;"> </mark><mark style="color:red;">Get clarity from Developers</mark></em></td></tr><tr><td></td><td>QueryFilter <br><em>(OData query option, value for $filter)</em></td><td><em><mark style="color:red;"><strong>SME Note:</strong></mark><mark style="color:red;"> </mark><mark style="color:red;">Get clarity from Developers</mark></em></td></tr><tr><td><strong>EntityListItem</strong></td><td>EntitySetOrNavProperty <em>(OData resource path)</em></td><td><em><mark style="color:red;"><strong>SME Note:</strong></mark><mark style="color:red;"> </mark><mark style="color:red;">Get clarity from Developers</mark></em></td></tr><tr><td></td><td>QueryFilter <br><em>(OData query option, value for $filter)</em></td><td><em><mark style="color:red;"><strong>SME Note:</strong></mark><mark style="color:red;"> </mark><mark style="color:red;">Get clarity from Developers</mark></em></td></tr><tr><td><strong>FormInput</strong></td><td>PropertyNav <br><em>(navigation portion of an OData resource path)</em></td><td><em><mark style="color:red;"><strong>SME Note:</strong></mark><mark style="color:red;"> </mark><mark style="color:red;">Get clarity from Developers</mark></em></td></tr><tr><td><strong>ReferenceInput</strong></td><td>PropertyNav <br><em>(navigation portion of an OData resource path)</em></td><td><em><mark style="color:red;"><strong>SME Note:</strong></mark><mark style="color:red;"> </mark><mark style="color:red;">Get clarity from Developers</mark></em></td></tr><tr><td></td><td>DataPathTemplate <br><em>(OData resource path)</em></td><td><em><mark style="color:red;"><strong>SME Note:</strong></mark><mark style="color:red;"> </mark><mark style="color:red;">Get clarity from Developers</mark></em></td></tr><tr><td></td><td>Query <br><em>(OData query option, value for $filter)</em></td><td><em><mark style="color:red;"><strong>SME Note:</strong></mark><mark style="color:red;"> </mark><mark style="color:red;">Get clarity from Developers</mark></em></td></tr></tbody></table>

### Navigation

<table><thead><tr><th width="189.65684058913322">Nav Type</th><th width="150">Field</th><th width="331">OData Syntax</th></tr></thead><tbody><tr><td><strong>ListLink</strong></td><td> DataPath</td><td><em><code>/EDBusiness</code></em></td></tr><tr><td></td><td>Query</td><td><p><strong>Open Code Box to add Query string:</strong></p><p><em><code>Deleted eq null and ShowListing eq true and (LicenceExpiry eq null or LicenceExpiry ge DateTime'{{=now}}')</code></em></p></td></tr><tr><td><strong>SingleListItem</strong></td><td>DataPath</td><td><em><code>/EDBusiness</code></em></td></tr></tbody></table>

### Application Objects

<table><thead><tr><th width="150">App Object</th><th width="183.2866134986382">Field</th><th>OData Syntax</th></tr></thead><tbody><tr><td><strong>AppObject</strong></td><td>DataServiceUrl <br>(<em>OData service root URL)</em></td><td>/<em><code>Fault({{= faultId}})</code></em></td></tr><tr><td></td><td>SortOrder <br><em>(OData query option, value for $orderby)</em></td><td><em><code>Created desc  OR  Deleted eq null</code></em></td></tr></tbody></table>

```html
public Object generateToken() throws Exception {
	try {
		String client_id = clientId;
		String client_secret = clientSecret;
		String grant_type = "client_credentials";
		URL url = null;
		InputStream stream = null;
		HttpURLConnection urlConnection = null;
	    {
	{
```

