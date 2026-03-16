import pandas as pd
import numpy as np

class AIRiskAssessmentEngine:
    """
    Strategic Risk Assessment Engine for Enterprise AI Adoption.
    Designed to evaluate AI applications against Ethical and Regulatory (EU AI Act) frameworks.
    """
    def __init__(self):
        self.risk_categories = {
            "UNACCEPTABLE": "Prohibited under EU AI Act (e.g., social scoring).",
            "HIGH": "Requires strict compliance (e.g., critical infrastructure, recruitment).",
            "LIMITED": "Specific transparency obligations (e.g., chatbots).",
            "MINIMAL": "No specific obligations (e.g., AI-enabled games)."
        }

    def assess_project(self, project_data):
        """
        Evaluates an AI project based on sensitivity and domain impact.
        """
        score = 0
        if project_data.get('critical_infrastructure'): score += 50
        if project_data.get('biometric_id'): score += 40
        if project_data.get('public_services'): score += 30
        if project_data.get('consumer_interaction'): score += 10
        
        if score >= 80:
            risk_level = "HIGH"
        elif score >= 30:
            risk_level = "LIMITED"
        else:
            risk_level = "MINIMAL"
            
        return {
            "project_name": project_data.get('name'),
            "risk_level": risk_level,
            "guidance": self.risk_categories[risk_level],
            "risk_score": score
        }

if __name__ == "__main__":
    engine = AIRiskAssessmentEngine()
    
    # Example assessment for a Recruitment AI system
    recruitment_ai = {
        "name": "HR-Triage-System-v1",
        "critical_infrastructure": False,
        "biometric_id": False,
        "public_services": True,
        "consumer_interaction": False
    }
    
    result = engine.assess_project(recruitment_ai)
    print(f"Risk Assessment for {result['project_name']}:")
    print(f"Level: {result['risk_level']} (Score: {result['risk_score']})")
    print(f"Regulatory Note: {result['guidance']}")
