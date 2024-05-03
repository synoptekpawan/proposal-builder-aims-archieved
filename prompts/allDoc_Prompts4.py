# def sectionTitle():
#     prompt = """
#             As an AI assistant, your task is to construct an title page using {title}.
#             Ensure the document is crafted in proper markdown format, reflecting the section title and subsections accurately. It should be direct and free from any external citations or documents; any discovered should be eliminated. Additionally, avoid incorporating unnecessary text simply to fill space. Any found should be omitted.
#             Do not add any Note section additionally.
#             """
#     return prompt

def sectionIndex():
    prompt = """
            As an AI assistant, your task is to construct an index page that effectively organizes the various sections of the document. This index should serve as a navigational guide, enabling easy access to each major section and their respective subsections as follows:
                -EXECUTIVE SUMMARY AND OVERVIEW
                -SCOPE OF WORK
                -TRANSITION PLAN AND APPROACH
                -ROLES AND RESPONSIBILITIES
                -CLIENT RESPONSIBILITIES
                -TECH STACK & SERVICES
                -COST AND TIMELINE
                -TERMS AND CONDITIONS
                -ASSUMPTIONS
            Ensure the document is crafted in proper markdown format, reflecting the section title and subsections accurately. It should be direct and free from any external citations or documents; any discovered should be eliminated. Additionally, avoid incorporating unnecessary text simply to fill space. Any found should be omitted.
            Do not add any Note section additionally.
            """
    return prompt

def sectionA():
    prompt = """
            As an AI assistant, your task is to modify a concise and impactful executive summary and overview for client. This should be structured as follows, adhering to a strict 200-word limit. Refere {background}, {mspOrg}, {clientOrg}, {objectives}:
                ### Client Background: Modify the client background with respect to the client's history, their role within their industry, and any pertinent background information that lays the foundation for the proposed work.
                ### Overview of Proposed Work: Outline the scope of services or solutions the managed service provider plans to offer. Summarize the key objectives and principal activities that define what is being proposed.
                ### Current Status: Detail the present situation or status quo that necessitates the proposed work, highlighting aspects of the client's operations, technology, or strategic stance that are relevant.
                ### Challenges Faced: Identify the main challenges or issues the client is dealing with, which the proposed work seeks to address.
                ### Proposed Value: Clarify the advantages or value the proposed work promises, focusing on how it aims to resolve the challenges identified and contribute to achieving the client's objectives.
            Ensure the document is crafted in proper markdown format, reflecting the section title and subsections accurately. It should be direct and free from any external citations or documents; any discovered should be eliminated. Additionally, avoid incorporating unnecessary text simply to fill space. Any found should be omitted.
            Do not add any Note section additionally.
            """
    return prompt

def sectionB():
    prompt = """
            As an AI assistant, you are to formulate and modify the scope of work from the extracted documents. This section is to be structured with the following subsections, compactly summarizing the project's key aspects in a single paragraph. Reference the project's objectives {objectives}, the technology in use {tech}, and user requirements {userRequirement}. Adhere strictly to a 150-word limit:
                ### Objective: List the primary goals and intentions behind the project from the. Refer objectives
                ### Scope: Outline the breadth of the project, highlighting what is to be included and potentially what is excluded. Refer user requirements.
                ### Approach: Describe the methodology and strategy for achieving the project objectives.
                ### Design: Provide an overview of the planned design elements and frameworks to be utilized.
                ### Deliverables: List the expected outcomes, products, or services to be delivered upon project completion. Refer user requirements.
            Ensure the document is crafted in proper markdown format, reflecting the section title and subsections accurately. Ensure the document is succinct and free from any external citations or documents; remove any that are found. Also, avoid inserting unnecessary text solely to extend the word count. Any found should be omitted.
            Do not add any Note section additionally.
            """
    return prompt

def sectionC():
    prompt = """
            As an AI assistant, your goal is to devise and modify a detailed transition strategy and methodology from the extracted documents. This section requires:
                ### Transition Plan: Develop a comprehensive plan detailing the steps for transitioning, which should align with the project's objectives {objectives}, the technology being implemented {tech}, and the needs of the users {userRequirement}. The plan should outline phases, key milestones, and any critical considerations necessary for a smooth transition.
                ### Transition Approach: Explain the approach behind the transition plan, including methodologies, tools, and processes to be utilized. This should also consider any potential challenges and the strategies to mitigate them, ensuring the transition aligns with the overall project goals and technology requirements.
            Ensure the document is crafted in proper markdown format, reflecting the section title and subsections accurately. Ensure the document is clear and to the point, omitting any external citations or documents. If any are found, they must be removed. Moreover, refrain from adding unnecessary text merely to meet a word count threshold. Any found should be omitted.
            Do not add any Note section additionally.
            """
    return prompt

def sectionD():
    prompt = """
            As an AI assistant, your mission is to develop and modify a comprehensive outline of the team configuration, including roles and duties. Refer the extracted documents.This section should feature:
                ### Team Structure: Craft a detailed enumeration of the team's hierarchy and structure for the managed service provider {mspOrg}. This should clearly delineate the organizational framework and how different roles interact within the team.
                ### Roles and Responsibilities: Elaborate on the specific roles within the team and their corresponding responsibilities. This description should be tied closely to the project's objectives {objectives}, the technology employed {tech}, and the requirements of the users {userRequirement}. Use bullet points to clearly and concisely present this information.
            Ensure the document is crafted in proper markdown format, reflecting the section title and subsections accurately. 
            Ensure the document is concise, focused, and devoid of any external citations or documents. Any discovered should be promptly removed. Also, avoid including superfluous text solely to extend the word count. Any found should be omitted.
            Do not add any Note section additionally.
            """
    return prompt

def sectionE():
    prompt = """
            As an AI assistant, your objective is to outline and modify client obligations within the document. This section should. Refer extracted documents:
                ### Responsibility Overview: Present a detailed list in bullet-point format that outlines the responsibilities of the client organization {clientOrg}. These responsibilities should be derived with reference to the project's objectives {objectives}, the technology being utilized {tech}, and the user requirements {userRequirement}.
            Ensure the document is crafted in proper markdown format, reflecting the section title and subsections accurately. 
            Ensure the content is clear and devoid of any external citations or documents. Should any be present, they must be excluded. Additionally, maintain brevity and relevance in the content, avoiding the addition of unnecessary text to fulfill a word count criterion. Any found should be omitted.
            Additionally, the content should be direct and to the point, without adding texts which summarizes the task to meet a word count threshold. Any found should be omitted.
            Do not add any sentences starting with "Note" or "Please note that"..
            """
    return prompt

def sectionF():
    prompt = """
            As an AI assistant, your assignment involves drafting a section on technology infrastructure and services. This section should:
                ### Tech Stack Overview: Provide a comprehensive breakdown of the technology stack {tech} utilized by the managed service provider {mspOrg}. This includes both hardware and software components that are integral to their operations
                ### Services Catalog: Detail the range of services offered by the managed service provider {mspOrg}. This should encapsulate all relevant services that leverage the aforementioned technology stack.
            Ensure the document is crafted in proper markdown format, reflecting the section title and subsections accurately. 
            Ensure the document remains concise and free from any citations or external documents. Should any be identified, they must be removed. 
            Additionally, the content should be direct and to the point, without adding texts which summarizes the task to meet a word count threshold. Any found should be omitted.
            Do not add any sentences starting with "Note" or "Please note that".
            """
    return prompt

# def sectionG():
#     prompt = """
#             As an AI assistant, your task is to craft a comprehensive cost and timeline document. This section should include two key components:
#             -## COST AND TIMELINE:
#                 -### Pricing Table: Construct a detailed pricing table that encompasses service names, descriptions, quantities, monthly recurring revenue (MRR), and extended MRR. Ensure to tailor this table in alignment with the specified technology {tech}.
#                 -### Task Timeline Table: Develop a task timeline table, resembling a Gantt chart, that takes into account the project's objectives {objectives} and the overall timeline {timeLine}. This table should thoughtfully incorporate the potential overlap between the completion of various objectives, providing a clear visual representation of the project's schedule. 
#             Ensure the document is crafted in proper markdown format, reflecting the section title and subsections accurately. Ensure the document is free of citations and external documents. Any found should be omitted. Additionally, avoid adding filler lines solely to meet a word count requirement. Any found should be omitted.
#             Do not add any Note section additionally.
#             """
#     return prompt

# def sectionAssumptions():
#     prompt = """
#                 As an AI assistant, your task is to modify the provided assumptions and tailor them for client.
#                 -## Section H: ASSUMPTIONS:
#                     Modify the {assumptions} to cater {clientOrg}
#                 Ensure the document is crafted in proper markdown format, reflecting the section title and subsections accurately. Ensure the document remains concise and free from any citations or external documents. Should any be identified, they must be removed. Additionally, the content should be direct and to the point, without adding unnecessary text to meet a word count threshold. Any found should be omitted.
#                 Do not add any Note section additionally.
#                 """
#     return prompt
