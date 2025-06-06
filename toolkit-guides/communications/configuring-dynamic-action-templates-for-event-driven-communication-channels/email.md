# Email

In this section, you will find detailed information about the supported fields that allow you to customise your email templates. These fields provide you with the flexibility to deliver personalised and engaging messages to your recipients. By understanding and utilising the configuration settings available, you can align your email communication with your brand and effectively capture the attention of your audience. Let's explore the dynamic fields available for customisation within Email:

1. To Address: The **To address** field allows you to specify the primary recipient/s of your message. To address box accepts a single email address or a semi-colon delimited list of email addresses. When you provide a list of email addresses the system will automatically iterate over the email addresses list when sending emails.&#x20;
2.  From Address: This field allows you to specify the sender of your email. \


    {% hint style="info" %}
    The From address field accepts a single email address. Ensure that your From address is a valid address otherwise some mail services will block your emails.
    {% endhint %}


3.  CC(Carbon Copy): The CC field in an email allows you to include additional recipients who will receive a copy of the email.\


    {% hint style="info" %}
    The CC box accepts a single email address or a semi-colon delimited list of email addresses. When you provide a list of email addresses the system will automatically iterate over the email addresses list when sending emails.&#x20;
    {% endhint %}


4.  BCC(Blind Carbon Copy): The BCC field functions similarly to the CC field, but with one key difference: the email addresses added to the BCC field remain hidden from all other recipients.&#x20;

    {% hint style="info" %}
    The BCC box accepts a single email address or a semi-colon delimited list of email addresses. When you provide a list of email addresses the system will automatically iterate over the email addresses list when sending emails.&#x20;


    {% endhint %}
5. Subject: The subject field allows you to provide a concise and descriptive summary of the email's content. It serves as a headline or title for the email, giving recipients a quick understanding of the purpose or topic.
6.  HTLM Body:  This setting allows you to use HTML or [Razor Pages](https://docs.microsoft.com/en-us/aspnet/core/razor-pages/?view=aspnetcore-6.0\&tabs=visual-studio) to write the body of your email template.&#x20;

    An example showing list rendering in the HTML Body:&#x20;

    ```aspnet
    @if (Model.Data.Items.Count == 0) { 
        <tr height="25px"> 
            <td style="border: thin solid silver;" colspan=2>No Reports Found</td> 
        </tr> 
        } else { 
                    foreach (var item in @Model.Data.Items) 
                        { 
                            <tr height="25px"> 
                                <td style="border: thin solid silver;"> 
                                    @item.FileName 
                                </td> 
                                <td style="border: thin solid silver;"> 
                                    @item.Received 
                                </td> 
                                <td style="border: thin solid silver;"> 
                                    @item.ProcessDate 
                                </td>
                                <td style="border: thin solid silver;"> 
                                    @item.ProcessTime 
                                </td> 
                                <td style="border: thin solid silver;"> 
                                    @item.Status 
                                </td> 
                            </tr>
                    } 
                }
        }    
    }
    ```


7. Text Body: This setting allows you to add the body of your template in text format. It is suited, although it can also be used for Emails, HTML Body is preferred for emails, as it produces a richer output.&#x20;
