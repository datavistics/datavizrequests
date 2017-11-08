import pandas as pd
import os

project_dir = os.path.join(os.getcwd(), os.pardir)
ci_path = os.path.join(project_dir, 'data', 'community_impact_scores.csv')
os_path = os.path.join(project_dir, 'data', 'opportunity_scores.csv')

df = pd.read_csv(os_path)
