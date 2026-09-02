from client import InfluencerBrandSafetyControversyAuditorClient

def main():
    client = InfluencerBrandSafetyControversyAuditorClient()
    res = client.audit_creator_safety_history('@foodie_adventures', 12)
    print('Influencer Brand Safety Auditor: ' + res['safety_audit_id'] + ' (' + res['brand_safety_clearance_verdict'] + ')')
    print('Safety Score: ' + str(res['brand_safety_score_pct']) + '% | Flagged Incidents: ' + str(res['flagged_controversies_count']))
    print('Toxicity Ratio: ' + str(res['profanity_toxicity_ratio_pct']) + '%')
    print('Heatmap URL: ' + res['historical_toxicity_heatmap_url'])

if __name__ == '__main__':
    main()
