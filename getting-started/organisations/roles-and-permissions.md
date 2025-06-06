# Roles and Permissions

## Overview

In the dynamic environment of the Toolkit, roles and permissions are foundational elements that ensure secure, efficient, and effective management of projects and teams within an organization. Understanding the distinct roles within the Toolkit and the permissions associated with each is crucial for users to navigate and utilise the system to its full potential.

Roles within the Toolkit are designed to cater to various levels of responsibility, from system-wide oversight to specific project tasks. These roles facilitate a structured approach to project management, allowing for clear delineation of duties and access control. Permissions linked to these roles define what actions a user can perform, ensuring that sensitive operations and information are accessible only to authorised individuals.

This section of the documentation aims to provide a comprehensive overview of the roles available within the Toolkit, detailing the permissions each role holds and the significance of these roles in the overall management of projects and organisational settings. Whether you are a Toolkit Administrator managing the system at a global level, an Organisational Administrator overseeing projects and teams, or a Developer contributing to project tasks, understanding your role and permissions is the first step towards maximising your effectiveness and contribution within the Toolkit.

By the end of this section, you will have a clear understanding of how roles and permissions work in tandem to support a secure, organised, and collaborative environment for all users involved in project and team management.

## Supported Roles

In modern project management, clear roles and responsibilities are essential for operational efficiency and success. The Toolkit is designed to support organisations with a well-defined role hierarchy, ensuring smooth project development from strategic oversight to detailed task execution.

The Toolkit framework assigns specific permissions and responsibilities to each team member, from Organisational Administrators to Developers and Designers. This structure fosters effective collaboration and access control, ensuring everyone contributes to the organisation's goals. By outlining this role hierarchy, we highlight the importance of organised collaboration and access control within the platform.

Understanding your role within this structure is the first step toward leveraging the Toolkit's full potential and driving your organisation's success. Whether you're managing the organisation or contributing your expertise, the Toolkit's framework helps maintain order and efficiency in collaborative projects.

1. **Toolkit Administrator**
   * Positioned at the highest level, the Toolkit Administrator has system-wide access and control over all organisations, projects, and users within the Toolkit. This role is responsible for the overall management and configuration of the Toolkit, including user and organisation approvals.
2. **Organisational Administrator**
   * Positioned at the top of the organisational hierarchy is the Organisational Administrator, who  has full control over all aspects of their organisation within the Toolkit. This includes managing users, creating teams and assigning team members, managing projects, assigning project owners, and overseeing the assignment of various teams and roles within the organisation. The Organisational Administrator can view all projects, reassign project ownership, and edit team compositions.
3. **Project Owner**
   * The Project Owner has control over a specific project, including visibility and editing rights. Initially, they are the sole individual with access to the project until they assign teams to it. The Project Owner can manage the project details, progress, and team assignments but operates under the governance of the Organisational Administrator.
4. **Teams (Developers, Lead Developers, Testers, DevOps etc.)**
   * Teams consist of individuals with roles such as Developer, Lead Developer, and other specialised roles defined within the organisation. These roles have specific permissions related to project development, such as editing project files, contributing to development tasks, and collaborating with other team members. The composition and assignment of these teams are managed by Project Administrators and overseen by Project Owners and the Organisational Administrator.
5. **Individual Contributors (Developers, Designers, Testers, DevOps etc.)**
   * At the project level, individual contributors work within their teams on specific tasks and projects. They have access and editing rights to projects they are assigned to and follow the directions of their team leaders (e.g., Lead Developers) and project governance established by Project Owners and Administrators.

## User Role Journey

This section outlines the user role journey from initial signup:

1. **Initial Signup**: A new user signs up to the Toolkit, representing a company or an individual with the intent to partner and build applications within the platform.
2. **Initial Role Assignment**: Upon signup, if the user is the first or only member of their organisation within the Toolkit, they are most likely to be made an Organisational Administrator. This role grants them the ability to manage the organisation's presence within the Toolkit, including project and user management.
3. **Role Expansion**: As the platform evolves, the plan is for Organisational Administrators to be able to invite new users into the organisation. These new users would immediately have access to the Toolkit, and their roles within the organisation can be set by the Organisational Administrator. This functionality aims to streamline the onboarding process for new users and facilitate role assignment within the organisation.
4. **Manual Role Assignment (Current State)**: Currently, if another member of the organisation needs access to the Toolkit, they must register independently. The Toolkit Administrator then manually assigns this new user to the organisation, after which the Organisational Administrator can set their roles, such as Developer, Lead Developer,  Tester , DevOps or any other defined role within the system.
5. **Toolkit Administrator Role**: The Toolkit Administrator plays a crucial role in this process, as they are responsible for approving registrations, creating organisations, and assigning users to organisations. This role is essential for the initial setup and ongoing management of user roles and organisation structures within the Toolkit.



## Supported Roles and Permissions

**Lead Developer**

| Component Name       | Environment | Access Rights |
| -------------------- | ----------- | ------------- |
| Build & Launch       | DEV         | Full (3)      |
| Deploy               | DEV         | Full (3)      |
| Deploy               | QA          | Full (3)      |
| Develop              | DEV         | Full (3)      |
| Download Backup      | DEV         | Full (3)      |
| Environment Settings | DEV         | Full (3)      |
| Environment Settings | PROD        | Full (3)      |
| Environment Settings | QA          | Full (3)      |
| Operate              | PROD        | Full (3)      |
| Operate              | QA          | Full (3)      |
| Project Settings     | DEV         | Full (3)      |
| Project Settings     | PROD        | Full (3)      |
| Project Settings     | QA          | Full (3)      |
| Communications       | DEV         | Full (3)      |
| Custom Classes       | DEV         | Full (3)      |
| Custom Website       | DEV         | Full (3)      |
| Data                 | DEV         | Full (3)      |
| Integrations         | DEV         | Full (3)      |
| Observability        | DEV         | Full (3)      |
| Observability        | PROD        | Full (3)      |
| Observability        | QA          | Full (3)      |
| Screens              | DEV         | Full (3)      |
| Deploy to QA         | DEV         | Full (3)      |
| Deployment history   | DEV         | Full (3)      |
| Deploy to Production | QA          | Full (3)      |
| Deployment history   | QA          | Full (3)      |

**Developer**

| Component Name       | Environment | Access Rights |
| -------------------- | ----------- | ------------- |
| Build & Launch       | DEV         | Full (3)      |
| Deploy               | DEV         | Full (3)      |
| Deploy               | QA          | Full (3)      |
| Develop              | DEV         | Full (3)      |
| Download Backup      | DEV         | Full (3)      |
| Environment Settings | DEV         | Full (3)      |
| Environment Settings | PROD        | Full (3)      |
| Environment Settings | QA          | Full (3)      |
| Operate              | PROD        | Full (3)      |
| Operate              | QA          | Full (3)      |
| Project Settings     | DEV         | Full (3)      |
| Project Settings     | PROD        | Full (3)      |
| Project Settings     | QA          | Full (3)      |
| Communications       | DEV         | Full (3)      |
| Custom Classes       | DEV         | Full (3)      |
| Custom Website       | DEV         | Full (3)      |
| Data                 | DEV         | Full (3)      |
| Integrations         | DEV         | Full (3)      |
| Observability        | DEV         | Full (3)      |
| Observability        | PROD        | Full (3)      |
| Observability        | QA          | Full (3)      |
| Screens              | DEV         | Full (3)      |
| Deploy to QA         | DEV         | Full (3)      |
| Deployment history   | DEV         | Full (3)      |
| Deploy to Production | QA          | Full (3)      |
| Deployment history   | QA          | Full (3)      |

**Operations**

| Component Name       | Environment | Access Rights |
| -------------------- | ----------- | ------------- |
| Environment Settings | DEV         | Full (3)      |
| Environment Settings | PROD        | Full (3)      |
| Environment Settings | QA          | Full (3)      |
| Develop              | DEV         | Full (3)      |
| Operate              | PROD        | Full (3)      |
| Operate              | QA          | Full (3)      |
| Observability        | DEV         | Full (3)      |
| Observability        | PROD        | Full (3)      |
| Observability        | QA          | Full (3)      |

**Viewer**

| Component Name  | Environment | Access Rights |
| --------------- | ----------- | ------------- |
| Build & Launch  | DEV         | View (1)      |
| Deploy          | DEV         | View (1)      |
| Deploy          | QA          | View (1)      |
| Develop         | DEV         | View (1)      |
| Download Backup | DEV         | View (1)      |
| Operate         | PROD        | View (1)      |
| Operate         | QA          | View (1)      |
| Communications  | DEV         | View (1)      |
| Custom Classes  | DEV         | View (1)      |
| Custom Website  | DEV         | View (1)      |
| Data            | DEV         | View (1)      |
| Integrations    | DEV         | View (1)      |
| Observability   | DEV         | View (1)      |
| Observability   | PROD        | View (1)      |
| Observability   | QA          | View (1)      |
| Screens         | DEV         | View (1)      |

#### Access Rights Legend

* **1**: View only
* **3**: Full access (view and edit)

This format organizes the roles and their permissions in a clear tabular manner, making it easier to understand which components each role has access to and in which environments.\
