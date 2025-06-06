# Manage Inheritance in the Data Model: Configuring Entity Hierarchy and Inheritance

Inheritance is a powerful feature supported by the ComUnity Developer Toolkit, allowing you to establish hierarchical relationships between entities. By default, every entity created in the Toolkit inherits from the BaseEntity, which serves as the base entity for all others. Each entity possesses a property called **Inherits from Entity**, which designates its parent entity. By customising the value of this property, developers can seamlessly implement inheritance and define the entity hierarchy according to their specific needs. In this comprehensive guide, we will explore how to configure entity inheritance, enabling you to leverage this essential feature for efficient data modelling and application development.&#x20;

To implement inheritance in the ComUnity Developer Toolkit and establish hierarchical relationships between entities, follow these steps:

1. Select the entity for which you want to configure permissions. In a Diagram view, click on the entity's header section with a grey background colour. An active entity is identified by a blue border, and none of its entity fields are active (active entity fields have a blue background colour). This action will open a properties dialog that displays the entity's global properties.
2. Within the properties dialog, locate and click on the **Inherits from Entity**  select dropdown by default this value is **BaseEntity**.
3. Select the desired parent entity from the dropdown.
4. Finally, click the **Save** button to persist your changes.

By following these steps, you can effectively implement inheritance in your data model and define the entity hierarchy within the ComUnity Developer Toolkit.
