# Customer IT Support Analysis

## Background and Overview

An open-source customer IT support dataset for a global brand has been obtained from Kaggle. Please find the dataset linked here: [Customer IT Support - Ticket Dataset](https://www.kaggle.com/datasets/tobiasbueck/multilingual-customer-support-tickets).

The fictitious company has significant amounts of data on its various departments, priority of issues, type of tickets, assigned tags/ categories, and queries' subject, body, and answers. This project thoroughly analyses and synthesises this data to uncover critical insights that will improve the business's quality of responses.

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
| Subject  | Subject of the customer's email                                               | String    |
| Body     | Body of the customer's email                                                  | String    |
| Answer   | The response provided by the helpdesk agent                                   | String    |
| Type     | The type of ticket as picked by the agent                                     | String    |
| Tags     | Tags/categories assigned to the ticket, split into ten columns in the dataset | String    |

For this analysis, the language column was filtered for English-only responses, and the linebreak code, \n\n, was removed from the queries' bodies and answers. This helped clarify the information, ensuring that all data points were clear and readable. This reduced the number of records to 16,338, a reduction of 42.85%.


## Executive Summary







4. Insights Deep Dive
5. Recommendations

































