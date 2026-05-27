import json
import csv
from datetime import datetime

# ============================================
# SONAR SYSTEM DESIGN TRADE STUDY ANALYZER
# ============================================

class SonarDesignAnalysis:
    def __init__(self):
        self.designs = {
            "Large Towed Array": {
                "detection_range_km": 15,
                "bearing_accuracy_deg": 2,
                "weight_kg": 2000,
                "power_kw": 15,
                "cost_m": 3.0,
                "deployment_time_min": 45,
                "complexity": "High"
            },
            "Hull-Mounted Fixed": {
                "detection_range_km": 6,
                "bearing_accuracy_deg": 12,
                "weight_kg": 300,
                "power_kw": 4,
                "cost_m": 0.8,
                "deployment_time_min": 5,
                "complexity": "Low"
            },
            "Lightweight Deployable Array": {
                "detection_range_km": 10,
                "bearing_accuracy_deg": 5,
                "weight_kg": 480,
                "power_kw": 7.8,
                "cost_m": 1.45,
                "deployment_time_min": 20,
                "complexity": "Medium"
            },
            "Autonomous AUV": {
                "detection_range_km": 12,
                "bearing_accuracy_deg": 6,
                "weight_kg": 150,
                "power_kw": 2,
                "cost_m": 2.0,
                "deployment_time_min": 30,
                "complexity": "Very High"
            }
        }
        
        self.requirements = {
            "detection_range_km": 10,
            "bearing_accuracy_deg": 5,
            "weight_kg": 500,
            "power_kw": 8,
            "cost_m": 1.5,
            "deployment_time_min": 30
        }
    
    def score_design(self, design_name):
        design = self.designs[design_name]
        scores = {}
        
        if design["detection_range_km"] >= self.requirements["detection_range_km"]:
            scores["range"] = 5
        elif design["detection_range_km"] >= 8:
            scores["range"] = 4
        elif design["detection_range_km"] >= 6:
            scores["range"] = 3
        else:
            scores["range"] = 1
        
        if design["bearing_accuracy_deg"] <= self.requirements["bearing_accuracy_deg"]:
            scores["accuracy"] = 5
        elif design["bearing_accuracy_deg"] <= 8:
            scores["accuracy"] = 4
        elif design["bearing_accuracy_deg"] <= 12:
            scores["accuracy"] = 3
        else:
            scores["accuracy"] = 1
        
        if design["weight_kg"] <= 300:
            scores["weight"] = 5
        elif design["weight_kg"] <= 500:
            scores["weight"] = 4
        elif design["weight_kg"] <= 1000:
            scores["weight"] = 3
        else:
            scores["weight"] = 1
        
        if design["power_kw"] <= 4:
            scores["power"] = 5
        elif design["power_kw"] <= 8:
            scores["power"] = 4
        elif design["power_kw"] <= 12:
            scores["power"] = 3
        else:
            scores["power"] = 1
        
        if design["cost_m"] <= 1.0:
            scores["cost"] = 5
        elif design["cost_m"] <= 1.5:
            scores["cost"] = 4
        elif design["cost_m"] <= 2.0:
            scores["cost"] = 3
        else:
            scores["cost"] = 1
        
        if design["deployment_time_min"] <= 15:
            scores["deployment"] = 5
        elif design["deployment_time_min"] <= 25:
            scores["deployment"] = 4
        elif design["deployment_time_min"] <= 40:
            scores["deployment"] = 3
        else:
            scores["deployment"] = 2
        
        return scores
    
    def calculate_overall_score(self, design_name):
        scores = self.score_design(design_name)
        
        weights = {
            "range": 0.20,
            "accuracy": 0.20,
            "weight": 0.15,
            "power": 0.15,
            "cost": 0.15,
            "deployment": 0.15
        }
        
        overall = sum(scores[key] * weights[key] for key in scores.keys())
        return overall, scores
    
    def rank_designs(self):
        rankings = {}
        
        for design_name in self.designs.keys():
            overall_score, detail_scores = self.calculate_overall_score(design_name)
            rankings[design_name] = {
                "overall_score": overall_score,
                "detail_scores": detail_scores,
                "specs": self.designs[design_name]
            }
        
        sorted_rankings = sorted(
            rankings.items(),
            key=lambda x: x[1]["overall_score"],
            reverse=True
        )
        
        return sorted_rankings
    
    def generate_report(self):
        rankings = self.rank_designs()
        
        report = []
        report.append("=" * 70)
        report.append("SONAR SYSTEM DESIGN TRADE STUDY - ANALYSIS REPORT")
        report.append("=" * 70)
        report.append(f"Generated: {datetime.now().strftime('%B %d, %Y at %H:%M')}")
        report.append("")
        
        report.append("REQUIREMENTS:")
        report.append(f"  • Detection Range: {self.requirements['detection_range_km']} km")
        report.append(f"  • Bearing Accuracy: ±{self.requirements['bearing_accuracy_deg']}°")
        report.append(f"  • Max Weight: {self.requirements['weight_kg']} kg")
        report.append(f"  • Max Power: {self.requirements['power_kw']} kW")
        report.append(f"  • Max Cost: ${self.requirements['cost_m']}M")
        report.append(f"  • Deployment Time: < {self.requirements['deployment_time_min']} min")
        report.append("")
        
        report.append("DESIGN RANKINGS (Highest Score = Best):")
        report.append("")
        
        for rank, (design_name, data) in enumerate(rankings, 1):
            report.append(f"{rank}. {design_name.upper()}")
            report.append(f"   Overall Score: {data['overall_score']:.2f}/5.00")
            report.append("")
            
            report.append("   Subscores:")
            for metric, score in data['detail_scores'].items():
                report.append(f"     • {metric.replace('_', ' ').title()}: {score}/5")
            
            report.append("")
            report.append("   Specifications:")
            for spec, value in data['specs'].items():
                if spec == "cost_m":
                    report.append(f"     • Cost: ${value}M")
                elif spec == "weight_kg":
                    report.append(f"     • Weight: {value} kg")
                elif spec == "power_kw":
                    report.append(f"     • Power: {value} kW")
                elif spec == "detection_range_km":
                    report.append(f"     • Detection Range: {value} km")
                elif spec == "bearing_accuracy_deg":
                    report.append(f"     • Bearing Accuracy: ±{value}°")
                elif spec == "deployment_time_min":
                    report.append(f"     • Deployment Time: {value} min")
                elif spec == "complexity":
                    report.append(f"     • Complexity: {value}")
            
            report.append("")
        
        best_design = rankings[0][0]
        best_score = rankings[0][1]['overall_score']
        
        report.append("=" * 70)
        report.append("RECOMMENDATION:")
        report.append("=" * 70)
        report.append(f"Selected Design: {best_design}")
        report.append(f"Overall Score: {best_score:.2f}/5.00")
        report.append("")
        report.append("Rationale:")
        report.append(f"  {best_design} provides the best balance of:")
        report.append("  • Meets all performance requirements")
        report.append("  • Acceptable weight and power constraints")
        report.append("  • Cost-effective solution")
        report.append("  • Realistic development timeline")
        report.append("")
        
        return "\n".join(report)
    
    def generate_csv_report(self, filename="sonar_analysis_results.csv"):
        rankings = self.rank_designs()
        
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            writer.writerow([
                "Design", "Overall Score", "Range Score", "Accuracy Score",
                "Weight Score", "Power Score", "Cost Score", "Deployment Score",
                "Detection Range (km)", "Bearing Accuracy (°)", "Weight (kg)",
                "Power (kW)", "Cost ($M)", "Deployment Time (min)"
            ])
            
            for design_name, data in rankings:
                scores = data['detail_scores']
                specs = data['specs']
                
                writer.writerow([
                    design_name,
                    f"{data['overall_score']:.2f}",
                    scores['range'],
                    scores['accuracy'],
                    scores['weight'],
                    scores['power'],
                    scores['cost'],
                    scores['deployment'],
                    specs['detection_range_km'],
                    specs['bearing_accuracy_deg'],
                    specs['weight_kg'],
                    specs['power_kw'],
                    specs['cost_m'],
                    specs['deployment_time_min']
                ])
        
        return filename

if __name__ == "__main__":
    print("Starting Sonar Design Analysis...\n")
    
    analyzer = SonarDesignAnalysis()
    
    report = analyzer.generate_report()
    print(report)
    
    with open("ANALYSIS_REPORT.txt", "w") as f:
        f.write(report)
    print("\n✓ Text report saved: ANALYSIS_REPORT.txt")
    
    csv_file = analyzer.generate_csv_report()
    print(f"✓ CSV data saved: {csv_file}")
    
    print("\n" + "="*70)
    print("ANALYSIS COMPLETE")
    print("="*70)
