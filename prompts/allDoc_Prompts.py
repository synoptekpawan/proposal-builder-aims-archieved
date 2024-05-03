def rfp_response_Main():
    prompt = """
            You are a professional document writer. Create a rfp response document for {approach}. 
            First create a separate tile page with {title}
            Also prepare a separate index page which would contain all sections and subsections with page number outlined below.
            Prepare the document with content for {title}, {approach}, {tech}, {objectives} & {userRequirement}.            
            It should contain following sections:
            -Section A: EXECUTIVE SUMMARY AND OVERVIEW:
                Prepare overview of {mspOrg} offerings which talks about following. 
                Use bullets points if necessary to emphasize. Prepare detail content.
                    -Background.
                        Prepare {background} of overall work envisaged in the engagement.
                        Also add current state, pain points and value proposition of offered solution.
                        Use bullets points to emphasize more.
                        Prepare detail content.
                    -Objectives.
                        Prepare business {objectives} in addition to technical goals to be achieved.
                        Use bullets points to emphasize more.
                        Prepare detail content.
            -Section B: SCOPE OF WORK:
                This gives details of {mspOrg} proposed solution and approach. 
                STRATEGIC ROADMAP DEVELOPMENT – ENVISION. Overview of Engagement & Transformation, Also discuss about the transition approach. Prepare a table if required.
                It discuss about the objectives, tech stack outlined in user requirements in subsections and in every objective or subsection it talks about:
                    -Objective
                    -Scope
                    -Approach
                    -Design
                    -Deliverables
                Prepare detail content.
            -Section C: INTEGRATED SOLUTION APPROACH
                This gives details of {mspOrg} approach in following subsections
                    -BUSINESS MODEL
                    -INTEGRATED SERVICE PORTFOLIO
                    -BUSINESS DRIVEN APPROACH
                    -CUSTOMER EXPERIENCE
                Prepare detail content.
            -Section D: TECH STACK & SERVICES
                This gives details about tech stack and services offered by {tech} from {mspOrg}.
            -Section E: PARTNERSHIP OPTION
                This gives details of partnership option like virtual captive centre and outlines its requirements, 
                conditions and responsibilities of partners along with partnership contract term. Prepare detail content for this.
            -Section F: COST AND TIMELINE
                -It give the overview of pricing and cost included. It provides well tabulated pricing with service names, description, Qty, MRR, Extended MRR. Generate the sample table.
                -Prepare task timeline table by considering above discussed objectives and the number of weeks {timeLine}. 
                Also highlight which objective will be completed in which week. Could consider overlap of task completions in timeline table.
            -Section G: ASSUMPTIONS:
                -These contains minimum 10 basic assumptions with some custom assumptions related to client's responsibility. Use bullets points to list assumptions and terms & conditions. Prepare detail content.
            -Section H: TERMS AND CONDITIONS
                -These contains the terms and conditions with some customizations with respect to scope of work and related to client's responsibility. Use bullets points to list terms & conditions. Prepare detail content.
            -Section I: APPROVAL
                -Prepare a table for approval which contains Name, Title, Date from both parties.
            -Section J: APPENDIX – FAQs:
                -This contains all FAQs related to RFP response document. Use bullet points to show the FAQs and also provide answers for each FAQs. Prepare detail content.
            """
    return prompt

def statement_of_work_Main():
    prompt = """
            You are a professional document writer. Create a statement of work document for {approach}. 
            First create a separate tile page with {title}
            Also prepare a separate index page which would contain all sections and subsections outlined below with page number .
            Prepare the document with content for {title}, {approach}, {tech}, {objectives} & {userRequirement}.
            It should contain following sections:
            -Section A: EXECUTIVE SUMMARY AND OVERVIEW:
                Prepare overview of {mspOrg} offerings which talks about following. 
                Use bullets points if necessary to emphasize. Prepare detail content.
                    -Background.
                        Prepare {background} of overall work envisaged in the engagement.
                        Also add current state, pain points and value proposition of offered solution.
                        Use bullets points to emphasize more.
                        Prepare detail content.
                    -Objectives.
                        Prepare bullets points for business {objectives} in addition to technical goals to be achieved.
                        Prepare detail content.
                
            -Section B: SCOPE OF WORK: 
                Prepare content for each {objectives} around {tech} in following subsections.
                The subsections are:
                    -Scope
                    -Approach
                    -Design
                    -Deliverables
                Prepare detail content.
            -Section C: TRANSITION PLAN AND APPROACH
                Prepare bullet points for {mspOrg} transition plan and approach. Prepare detail content.
            -Section D: ROLES AND RESPONSIBILITIES
                Prepare detailed points for {mspOrg} team structure along with their roles and responsibilities in bullets points to emphasize more.
                Prepare detail content.
            -Section E: CLEINT RESPONSIBILITIES
                Prepare points for {clientOrg} roles and responsibilities in bullets points to emphasize more.
                Prepare detail content.
            -Section F: TECH STACK & SERVICES
                Prepare the details about tech stack and services offered by {tech} from {mspOrg} in bullets points to emphasize more.
                Prepare detail content.
            -Section G: DELIVERABLES
                Prepare the lists of deliverables using the scope of work section in bullets points to emphasize more.
                Prepare detail content.
            -Section H: COST AND TIMELINE
                It give the overview of pricing and cost included. It provides well tabulated pricing with service names, description, Qty, MRR, Extended MRR. Generate the sample table.
                Prepare task timeline table just like gant chart by considering above discussed objectives and the number of weeks {timeLine}. 
                Also highlight which objective will be completed in which week. Also consider overlap of task completions in timeline table.
            -Section I: TERMS AND CONDITIONS
                These contains the terms and conditions with some customizations with respect to scope of work and related to client's responsibility. 
                Use bullets points to list terms & conditions. Prepare detail content.
            -Section J: ASSUMPTIONS:
                Prepare minimum 10 basic assumptions. Add some custom assumptions related to client's responsibility
                Use bullets points to list assumptions and terms & conditions. Prepare detail content.
            -Section K: APPROVAL
                Prepare a table for approval which contains Name, Title, Date from {clientOrg} & {mspOrg}. 
            
            """
    return prompt

def change_Order_Main():
    prompt = """
            You are a professional document writer. Create a change of order document for {approach}. 
            First create a separate tile page with {title}
            Also prepare a separate index page which would contain all sections and subsections with page number outlined below.
            Prepare the document with content for {title}, {approach}, {tech}, {objectives} & {userRequirement}.
            It should contain following sections:
            -Section A: EXECUTIVE SUMMARY AND OVERVIEW:
                Prepare overview of {mspOrg} offerings which talks about following. 
                Use bullets points if necessary to emphasize. Prepare detail content.
                    -Background.
                        Prepare {background} of overall work envisaged in the engagement.
                        Also add current state, pain points and value proposition of offered solution.
                        Use bullets points to emphasize more.
                        Prepare detail content.
                    -Objectives.
                        Prepare business {objectives} in addition to technical goals to be achieved.
                        Use bullets points to emphasize more.
                        Prepare detail content.
            -Section C: SCOPE OF SERVICES:
                -This gives details of {mspOrg} proposed solution and approach. 
                It discuss about the objectives, tech stack outlined in user requirements in subsections and in every objective or subsection it talks about:
                    -Objective
                    -Scope
                    -Approach
                    -Design
                    -Deliverables
            -Section D: APPROACH
                This gives details of {mspOrg} approach in following subsections. Prepare detail content. 
            -Section E: COST AND TIMELINE
                -It give the overview of pricing and cost included. It provides well tabulated pricing with service names, description, Qty, MRR, Extended MRR. Generate the sample table.
                -Prepare task timeline table by considering above discussed objectives and the number of weeks {timeLine}. 
                Also highlight which objective will be completed in which week. Could consider overlap of task completions in timeline table.
            -Section F: TERMS AND CONDITIONS
                -These contains the terms and conditions with some customizations with respect to scope of work and related to client's responsibility. Use bullets points to list terms & conditions. Prepare detail content.
            -Section G: ASSUMPTIONS:
                -These contains minimum 10 basic assumptions with some custom assumptions related to client's responsibility. Use bullets points to list assumptions and terms & conditions. Prepare detail content.
            -Section H: APPROVAL
                -Prepare a table for approval which contains Name, Title, Date from both parties.
            
            """
    return prompt


def new_Logo_Main():
    prompt = """
            You are a professional document writer. Create a new logo document for {approach}. 
            First create a separate tile page with {title}
            Also prepare a separate index page which would contain all sections and subsections with page number outlined below.
            Prepare the document with content for {title}, {approach}, {tech}, {objectives} & {userRequirement}.
            It should contain following sections:
            -Section A: EXECUTIVE SUMMARY AND OVERVIEW:
                Prepare overview of {mspOrg} offerings which talks about following. 
                Use bullets points if necessary to emphasize. Prepare detail content.
                    -Background.
                        Prepare {background} of overall work envisaged in the engagement.
                        Also add current state, pain points and value proposition of offered solution.
                        Use bullets points to emphasize more.
                        Prepare detail content.
                    -Objectives.
                        Prepare business {objectives} in addition to technical goals to be achieved.
                        Use bullets points to emphasize more.
                        Prepare detail content.
                
            -Section B: SCOPE OF WORK:
                -This gives details of {mspOrg} proposed solution and approach. 
                It discuss about the objectives, tech stack outlined in user requirements in subsections and in every objective or subsection it talks about:
                    -Objective
                    -Scope
                    -Approach
                    -Design
                    -Deliverables
                Prepare detail content.
            -Section C: TRANSITION PLAN AND APPROACH
                This gives details of {mspOrg} transition plan and approach in bullets points to emphasize. Prepare detail content.
            -Section D: ROLES AND RESPONSIBILITIES
                This gives details of team structure along with their roles and responsibilities in bullets points to emphasize. Prepare detail content.
            -Section E: TECH STACK & SERVICES
                This gives details about tech stack and services offered by {tech} from {mspOrg}.
            -Section F: DELIVERABLES
                This lists deliverables from the scope of work.
            -Section G: COST AND TIMELINE
                -It give the overview of pricing and cost included. It provides well tabulated pricing with service names, description, Qty, MRR, Extended MRR. Generate the sample table.
                -Prepare task timeline table by considering above discussed objectives and the number of weeks {timeLine}. 
                Also highlight which objective will be completed in which week. Could consider overlap of task completions in timeline table.
            -Section H: ASSUMPTIONS:
                -These contains minimum 10 basic assumptions with some custom assumptions related to client's responsibility. Use bullets points to list assumptions and terms & conditions. Prepare detail content.
            -Section I: TERMS AND CONDITIONS
                -These contains the terms and conditions with some customizations with respect to scope of work and related to client's responsibility. Use bullets points to list terms & conditions. Prepare detail content.
            -Section J: APPROVAL
                -Prepare a table for approval which contains Name, Title, Date from both parties.
            
            """
    return prompt

