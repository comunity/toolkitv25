# Triggering the Communication Service

The [CommsService.TriggerEvent()](triggering-the-communication-service.md#commsservice.trigger) function has six required arguments which are outlined in the table below:

<table><thead><tr><th width="246">Argument</th><th width="177.56342166234055">Type/Return Type</th><th>Description/Typical Value</th></tr></thead><tbody><tr><td>appName</td><td>String</td><td><code>Config.AppName()</code></td></tr><tr><td>eventName</td><td>String</td><td>A unique name of your event defined under <strong>Configuration</strong> -> <strong>Communication Services</strong></td></tr><tr><td>payload</td><td>JSON</td><td>Use the <code>ComsServices.JsonSerialize()</code> function to serialise the current instance of your class into JSON</td></tr><tr><td>url</td><td>String</td><td><code>Config.ComsService()</code></td></tr><tr><td>userName</td><td>String</td><td><code>Config.UserName()</code></td></tr><tr><td>password</td><td>String</td><td><code>Config.Password()</code></td></tr></tbody></table>

To trigger the Communication Service, follow these steps:

1. Open your project and navigate to Data.
2. Select Diagram or List to view your Data Model.
3. Locate and select the entity for which you want to configure communications. In a Diagram view, click on the entity's header section with a grey background colour. An active entity is identified by a blue border, and none of its entity fields are active (active entity fields have a blue background colour).&#x20;
4. This action will open a properties dialog that displays the entity's global properties.
5. Within the properties dialog, locate **Custom Code** you can expand the text editor by clicking on the ![](<../../.gitbook/assets/image (238).png>) icon.  &#x20;
6. Now, you need to identify and select a change interceptor to initiate the `ComsService.Trigger()` function. If the custom code has already been auto-generated, you can proceed with selecting an appropriate change interceptor. However, if the custom code hasn't been auto-generated, you have the option to define your own partial class. Within this class, you can invoke the `ComsService.Trigger()` function using the interceptor of your choice as show&#x6E;_(check line 66 in the code block below)_:

{% code lineNumbers="true" %}
```csharp
// Copyright (c) ComUnity 2017

using ComUnity.DataServices;
using ComUnity.DataServices.DomainUtility.Exceptions;
using ComUnity.DataServices.DomainUtility.Security;
using ComUnity.DataServices.ServiceUtility;
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Data.Entity;
using System.Data.Entity.ModelConfiguration.Conventions;
using System.Data.Services;
using System.Data.Services.Providers;
using System.Linq;
using System.Linq.Expressions;
using System.Web;

namespace CaseComms.Models
{
	public partial class Case
	{
		// START auto-generated - CTOR
		public Case() : base()
		{
		// END auto-generated, add custom code below this line
		
		}
		
		// START auto-generated - OnAdd
		public override void OnAdd(CaseCommsContext context)
		{
			base.OnAdd(context);
			CaseStatus status = context.Set<CaseStatus>().FirstOrDefault();
			Status = status ?? throw new GeneralException(400, "General", "No status defined in database!");
			context.SaveChanges();
			DateTime dt = DateTime.Now;
			string refString = dt.ToShortDateString() + "-" + CaseId;
			ReferenceNumber = refString;
			var toAddress = Config.CaseEmail();
			var an = Config.AppName();
			var cs = Config.ComsService();
			if (toAddress != null && an != null && cs != null)
			{
			    var payload = ComsServices.JsonSerialize(this);
			    ComsServices.TriggerEvent(an, "OnAddCase", payload, cs, Config.ComsServiceUsername(), Config.ComsServicePassword());
			}
		
		// END auto-generated, add custom code below this line
		
		}
		
		// START auto-generated - OnChange
		public override void OnChange(CaseCommsContext context)
		{
			base.OnChange(context);
			int prevStatus = context.Entry(this).OriginalValues.GetValue<int>("StatusCaseStatusId");
			if (StatusCaseStatusId != prevStatus)
			{
				var an = Config.AppName();
				var cs = Config.ComsService();
				if (an != null && cs != null)
				{
					var payload = ComsServices.JsonSerialize(this);
					// ComsServices.TriggerEvent() invocation
					ComsServices.TriggerEvent(an, "OnChangeCase", payload, cs, Config.ComsServiceUsername(), Config.ComsServicePassword());
				}
			}
		
		// END auto-generated, add custom code below this line
		
		}
		
		// START auto-generated - OnDelete
		public override void OnDelete(CaseCommsContext context)
		{
			base.OnDelete(context);
		// END auto-generated, add custom code below this line
		
		}
		
		// START auto-generated - Filter start
		public static Expression<Func<Case,bool>> Filter(CaseCommsContext context)
		{
			Expression<Func<Case, bool>> filter = o => true;
		// END auto-generated, add custom code below this line
			
		// START auto-generated - Filter end
			return filter;
		}
		// END auto-generated, add custom code below this line
		
		// START auto-generated - OnSeed
		public static void OnSeed(CaseCommsContext context)
		{
		// END auto-generated, add custom code below this line
		
		}
	}
}

```
{% endcode %}

After triggering the Communication Service by adding the code to invoke the `ComsService.Trigger()` function, the next step is to configure the event action and templates.
