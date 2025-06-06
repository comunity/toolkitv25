# Creating Entity Associations: Configuring Table Links

In the ComUnity Developer Toolkit, you have the power to establish and configure various types of entity associations and relationships within your data model. This section focuses on creating entity associations using Table Links, a powerful feature that enables you to define connections between entities and add foreign key properties.

Whether you need to establish one-to-many, one-to-one, or other types of relationships, the Toolkit offers flexible options to meet your requirements. With Table Links, you can create robust associations between entities, ensuring data integrity and efficient data retrieval.

By leveraging Table Links, you can seamlessly integrate related entities and enable cascading actions, such as automatic updates or deletions. This enhances the consistency and efficiency of your data model, providing a solid foundation for building sophisticated applications.

In the upcoming section, we will explore the step-by-step process of creating entity associations using Table Links. You will learn how to establish relationships, define foreign key properties, and configure the desired behaviour of the associations.

To create Table Links and establish entity associations follow these steps:

1. In your project settings in the Toolkit navigate to Data then select Diagram or List to view your Data Model.
2. Locate the <img src="../../.gitbook/assets/image (277).png" alt="" data-size="original"> icon, this icon allows you to add a new Table Link.
3. Click ![](<../../.gitbook/assets/image (245).png>) icon, and an **Add a new table link** modal window will appear on your screen.
4. In the **From Entity** box, select the entity from which you want to start the link. In the **To Entity** box, select the entity to which you want to link. The order of selection does not matter, as table links have no direction.
5. Finally, click on the **Add table link** button to create your table link.

Once you have created your table link, it will appear as a line connecting the entities in a Diagram view. In the expanded view of an entity, the table link will be displayed as a field with a ![](<../../.gitbook/assets/image (191).png>) icon. When you click on a table link, it will be selected and indicated by turning blue in the Diagram view or having a blue background in the List view, as shown in the images below. This visual indication helps you identify and interact with the table link easily.

Upon selecting a table link, a properties dialog will appear, providing you with a comprehensive set of options and settings to configure the behaviour and characteristics of the association. You can customise the table link properties according to your specific requirements.

For a detailed description and explanation of each table link property, please refer to the [table](creating-entity-associations-configuring-table-links.md#table-link-properties) below.

<figure><img src="../../.gitbook/assets/image (204).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (298).png" alt=""><figcaption></figcaption></figure>

### Table Link Properties

<table><thead><tr><th width="222.7956204379562">Association name</th><th width="335">Function</th><th>Value selection</th></tr></thead><tbody><tr><td><strong>From Entity</strong> </td><td>Identifies the source entity</td><td>Select an Entity from the  list of Tables in the dropdown.</td></tr><tr><td><strong>From Relationship</strong></td><td>Identifies the type of relationship</td><td>Select one of:<br>Many | 0..1 (Zero or One) | 1 (On</td></tr><tr><td><strong>From Entity Navigation  Name</strong></td><td><p>Each originating Table Link must be identified with a name. </p><p><em>For more information: Go to</em> <br>Entity framework relationships @ <a href="https://docs.microsoft.com/en-us/ef/ef6/fundamentals/relationships">https://docs.microsoft.com/en-us/ef/ef6/fundamentals/relationships</a></p></td><td>Label the Table Link</td></tr><tr><td><strong>To Entity</strong></td><td>Identifies the target entity</td><td>Select an Entity from the  list of Tables in the dropdown.</td></tr><tr><td><strong>To Relationship</strong></td><td>Identifies the type of relationship</td><td>Select one of:<br>Many | 0..1 (Zero or One) | 1 (One)</td></tr><tr><td><strong>To Entity Navigation  Name</strong></td><td><p>Each target Table Link must be identified with a name. </p><p><em>For more information: Go to</em> <br>Entity framework relationships @ <a href="https://docs.microsoft.com/en-us/ef/ef6/fundamentals/relationships">https://docs.microsoft.com/en-us/ef/ef6/fundamentals/relationships</a></p></td><td>Label the Table Link</td></tr><tr><td><strong>Add Foreign Key Property</strong></td><td><p>It is recommended that you include properties in the model that map to foreign keys in the database. With foreign key properties included, you can create or change a relationship by modifying the foreign key value on a dependent object. Using foreign keys is even more essential when working with disconnected entities. Note: that when working with 1-to-1 or 1-to-0..1 relationships, there is no separate foreign key column, the primary key property acts as the foreign key and is always included in the model.<br><em>For more information: Go to</em> <br><em>Entity framework relationships @</em></p><p> <a href="https://docs.microsoft.com/en-us/ef/ef6/fundamentals/relationships"><em>https://docs.microsoft.com/en-us/ef/ef6/fundamentals/relationships</em></a></p></td><td>Select the checkbox to set a foreign key</td></tr></tbody></table>
