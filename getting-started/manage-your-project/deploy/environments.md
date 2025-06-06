# Environments

Our deployment process utilises three distinct environments, each colour-coded to prevent deployment errors by providing immediate visual differentiation. This system ensures that modifications and updates are made in the correct environment, safeguarding the development and deployment pipeline.

{% embed url="https://drive.google.com/file/d/1K_rX3HYA6NsQZB32vdbKubamA8I9g0Ww/view?usp=sharing" %}
Deployment environments offered in the Toolkit
{% endembed %}

## Development **Environment(Green)**

This serves as the default playground for developers with relevant access. They can write, test, and refine code freely within this environment before moving it further down the pipeline. This isolated space ensures code integrity and consistency across the team.

<figure><img src="../../../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

## QA/Testing **Environment(Vibrant Purple)**

After the development phase, code is promoted to the QA/Testing environment. Here, rigorous testing takes place to ensure the application functions flawlessly under various conditions. This environment closely resembles the production setup, allowing for the identification and resolution of potential issues before reaching end users.

<figure><img src="../../../.gitbook/assets/image (91).png" alt=""><figcaption></figcaption></figure>

## **Production Environment (Deep Purple)**

The final stage in the deployment process is the production environment. This is where the fully tested and stable application is made live and accessible to end-users. Deployments to this environment are critical and require meticulous planning and execution to ensure service continuity and reliability.

<figure><img src="../../../.gitbook/assets/image (92).png" alt=""><figcaption></figcaption></figure>

By employing these colour distinctions—green for Development, vibrant purple for QA/Testing, and deep purple for Production—we enhance operational safety by reducing the risk of cross-environment deployment errors, thereby supporting the overall quality and success of the application.
