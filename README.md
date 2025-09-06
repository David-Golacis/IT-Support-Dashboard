# Customer IT Support Analysis

## Background and Overview

An open-source customer IT support dataset for a global brand has been obtained from Kaggle. Please find the dataset linked here: [Customer IT Support - Ticket Dataset](https://www.kaggle.com/datasets/tobiasbueck/multilingual-customer-support-tickets).

The fictitious company has significant amounts of data for its application across various departments, including priority of issues, types of tickets, assigned tags/categories, and queries' subjects, bodies, and answers. This project thoroughly analyses and synthesises this data to uncover critical insights that will improve the business's quality of responses.

Insights and recommendations are provided on the following key areas:
- Evaluation of departmental workload distribution
- An analysis of the highest priority issues
- An assessment of the most frequent tags used
- Identification of commonly requested details in ticket responses

An interactive Power BI dashboard can be downloaded [here](https://github.com/David-Golacis/IT-Support-Dashboard/blob/main/IT%20Support%20Dashboard.pbix).

The dataset used can be found [here](https://github.com/David-Golacis/IT-Support-Dashboard/blob/main/Dataset/aa_dataset-tickets-multi-lang-5-2-50-version.csv).


## Data Structure Overview

The Customer IT Support dataset consists of one table with 28,587 records. Shown below is the structure of the database.

| Field    | Description                                                                   | Data Type |
|----------|-------------------------------------------------------------------------------|-----------|
| Queue    | Specifies the department to which the email ticket is routed                  | String    |
| Priority | Indicates the urgency and importance of the issue                             | String    |
| Language | Indicates the language in which the email is written                          | String    |
| Version  | Designates the version of the application used                                | Number    |
| Subject  | Subject of the customer's email                                               | String    |
| Body     | Body of the customer's email                                                  | String    |
| Answer   | The response provided by the helpdesk agent                                   | String    |
| Type     | The type of ticket as picked by the agent                                     | String    |
| Tags     | Tags/categories assigned to the ticket, split into ten columns in the dataset | String    |

For this analysis, the following amendments were made:
- The language column was filtered for English-only responses
- From the queries' bodies and answers, the linebreak code, \n\n, was removed
- A custom table aggregating the 

This helped clarify the information, ensuring that all data points were clear and readable. This reduced the number of records to 16,338, a reduction of 42.85%.


## Executive Summary

Key performance indicators show that the Technical Support department handles the majority of tickets by volume, 4,737, of the 16,338 total tickets raised, equating to 28.99%. From the total number of issues, 38.84% have been marked as high-priority incidents, indicating urgency and importance to the business. Additionally, 40.22% of problems have been assigned the incident type by an agent, showing that issues were related to unplanned interruption or a reduction in the quality of an IT service that directly impacts users' ability to perform their jobs. To further support this, the top 3 tags across all records signify concerns with the application's usability: Tech Support, IT, and Performance.

Below is the overview page from the Power BI dashboard, and more examples are included throughout the report.

![Executive overview]()


## Insights Deep Dive




## Recommendations

































