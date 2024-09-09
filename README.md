# airflow_learning
<img width="1000" alt="image" src="https://github.com/user-attachments/assets/fc448e81-d1b3-43c5-9447-a38ad235a108">


This repository has been created to learn, code and deep dive to Airflow concepts, its uses and functioning, to enable effective and best way to use the Airflow with Python.

**How much python is required for Apache Airflow ?**
  This question often comes in mind of an individual, or a person who just started to learn, how much python they required to learn and start writing airflow dags ?
  For startup, we just need fundamental understanding of Python :
  **1. Basic Python syntax**
       Variables
       Datatypes
       functions
       loops
       conditionals
       Data Structure [list, tuple, string, set, dictonary]

  **2.  Modules and Libraries**
        How to import and use various modules and libraries in Python ?

  **3.  Function and Classes**
         Airflow task are often written as Python functions, so you need to know
            How to define function and use functions ?
            Familarity with OOPS programming in Python

  **4. File Handling**
       Reading & writing files

  **5.  Error Handling**
        How to handle exceptions in Python ?

  **6.  Airflow uses Jinja Templating**, so basic templating knowledge can be helpful.

Before we start designing the airflow dags, lets first understand, 
  What is Airflow ? 
  What's before Airflow ?
  What is the use of Airflow ?
  Applications of Airflow ?
  Advantages and Disadvantages of Airflow ?
  Alternative of Airflow ?

**Airflow : [Apache Airflow]**
  Airflow is a open-source tool to programatically author, monitor and schedule **workflows**.
  It is robust platform used by Data engineers to orchastrate workflows or data piplines. 
  One can easily visulaize data pipline's:
    Dependency, Proggress, Logs, Errors, Code, Success and Failed status.

  From above defination, one question arieses ? What is the workflow, data pipline and orchestrationand? what its significance in Airflow ?

 ** Workflow :** Its a system to manager repetative processes and task which occur in a partiular order. 
  In other words, It is a set of tasks and steps which can be scheduled, intiated, and monitored. 
  Workflows are used to process, build application and process data.
  Workflows can appear as a series of steps in a checklist, or as a diagram that visualizes those steps.

  The following is an example of a simple support workflow:

  1.  Carl, a customer, **starts** a support request.
  2.  The open case is **assigned** to Sasha, a Support Representative.
  3.  Sasha receives the assigned case and asks Carl for information. While waiting for the reply, the case’s status is **pending**.
  4.  After Carl provides the requested information, Sasha replies with a solution and then updates the case’s status to **resolved**.
  5.  Carl receives the answer, as well as a survey link where he can provide feedback about his support request.
  6.  He is delighted with Sasha’s quick response and gives high ratings in the survey. The case’s status is updated to **closed**.

In this workflow, the steps are “start”, “assign”, “resolve”, and “close”. The states are “open”, “assigned”, “pending”, “resolved”, and “closed”. Steps move the process from state to state along a path until the workflow is completed.


**What are the benefits of using workflows?**
Workflows provide a set of repeatable steps and tasks that you can initiate, schedule, and monitor.

You can visualize workflows for observation, validate the workflow’s correctness, and monitor the operations in the workflow.

With workflows, businesses can achieve improved levels of reliability for distributed applications without adding additional complexity to their code. You can automate, optimize, and scale workflows at a granular level. 

**What do workflows bring to application architecture?**
Workflows promote logical separation between the control flow of your job's stepwise logic and the actual units of work that contain your unique business logic. With this division, you can manage, maintain, and scale the state machinery of your application separately from the core business logic.

As your business requirements change, you can easily change application logic without changing the underlying state machinery, task dispatch, and flow control.

**How do workflow services improve application architecture?**

  **Reduced errors:** Manual steps can lead to errors, which can be costly and slow down business processes. 
                       Workflow automation can help reduce errors and make systems more efficient. 
  
  **Improved collaboration:** Workflows can help solve communication issues and improve collaboration. 
 
  **Reduced redundancies:** Workflows can help reduce redundancies in steps and human error. 
 
  **Increased business compliance:** Workflows can help support business compliance. 
 
  **Lowered costs:** Workflows can help lower costs by guiding information and task flow more efficiently. 
 
  **Increased focus:** Workflows can help employees focus on higher-value work


**What are some common workflow use cases?**
Workflows can help with any computational problem or business process that can be divided into a series of steps. Workflows simplify managing jobs with interdependencies. Common use cases include:

**Application orchestration –** Coordinate loosely coupled microservices, each running in its own process and independently deployed, through communication of events. Combine serverless functions to build a web application with an asynchronous human approval step.

**Data processing –** Consolidate data from multiple data sets into unified reports, refine and reduce large data sets into useful formats, or coordinate multi-step analytics and machine learning workflows.

**DevOps and IT automation –** Build tools for continuous integration and deployment, or create event-driven applications that automatically respond to changes in infrastructure.

**Ecommerce –** Automate mission-critical business processes, such as order fulfillment and inventory tracking.

**Web applications –** Implement robust user registration processes and authentication, optionally integrating steps for auditing and enhanced security.

**Machine learning –** Run extract, transform, and load (ETL) jobs to build, train, and deploy a machine learning model. For example, collecting and processing image data to detect objects within a video stream, to add bounding boxes, or to provide visual and metadata information for data cataloging.

**Security automation –** Scheduled analysis or security incident response initiated by managed resource events, with customized workflows that invoke audit and notification steps depending on business rules.

**Media processing –** Extract data from PDF documents or images for processing. Split and transcode video using massive parallelization. 

  
  
  

  
  
  
  
  



     
