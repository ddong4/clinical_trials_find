Time Breakdown

* ~1 hr - Understand problem, draft out in excalidraw
* 30 min - Setup general folder structure, assisted .vscode json by copilot
* 30 min - github actions to send to ghcr and then self-hosting
    * ghcr.io/ddong4/clinical_trials_find-backend:main
    * ghcr.io/ddong4/clinical_trials_find-frontend:main
* 30 min - gemini responses. Using flash because $. This gave lots of null responses, so added in simple retry
* 15 min - made transcript simulation based off of user journey setup with chatgpt https://chatgpt.com/share/68e8842b-ce4c-8006-8821-0cfb8bff9f54
* 30 min - Figuring out clinical trials API. Started by viewing request done for a basic search on website, see Loose Notes below
* 30 min - Extracting keywords from transcript. For now, getting diagnosis is most important
* 15 min - Hook up with Frontend, display response
* 15 min - Configure my reverse proxy and cloudflare to expose website
* 2 hrs - understanding openapi-client codegen and making basic package with clinical trials spec
* 30 min - getting build to work with local py package
* 30 min - Add in integration backend and frontend, put in dataframe and show top <=10 results

# Loose Notes
## Clinical Trials API
Due to limited time, use simple /studies API call. 
Using website and searching "Plantar Fasciitis", I grabbed the request url below

https://clinicaltrials.gov/api/int/studies?cond=Plantar%20Fasciitis&aggFilters=&checkSpell=true&from=0&limit=10&fields=OverallStatus%2CLastKnownStatus%2CStatusVerifiedDate%2CHasResults%2CBriefTitle%2CCondition%2CInterventionType%2CInterventionName%2CLocationFacility%2CLocationCity%2CLocationState%2CLocationCountry%2CLocationStatus%2CLocationZip%2CLocationGeoPoint%2CLocationContactName%2CLocationContactRole%2CLocationContactPhone%2CLocationContactPhoneExt%2CLocationContactEMail%2CCentralContactName%2CCentralContactRole%2CCentralContactPhone%2CCentralContactPhoneExt%2CCentralContactEMail%2CGender%2CMinimumAge%2CMaximumAge%2CStdAge%2CNCTId%2CStudyType%2CLeadSponsorName%2CAcronym%2CEnrollmentCount%2CStartDate%2CPrimaryCompletionDate%2CCompletionDate%2CStudyFirstPostDate%2CResultsFirstPostDate%2CLastUpdatePostDate%2COrgStudyId%2CSecondaryId%2CPhase%2CLargeDocLabel%2CLargeDocFilename%2CPrimaryOutcomeMeasure%2CSecondaryOutcomeMeasure%2CDesignAllocation%2CDesignInterventionModel%2CDesignMasking%2CDesignWhoMasked%2CDesignPrimaryPurpose%2CDesignObservationalModel%2CDesignTimePerspective%2CLeadSponsorClass%2CCollaboratorClass&columns=conditions%2Cinterventions%2Ccollaborators&highlight=true&sort=%40relevance

Clinical Trials website output UI is nice, honestly would do an iframe haha
sort seems default as relevance. Need to adjust Study Status param

request filtered by Recruiting
https://clinicaltrials.gov/api/int/studies?cond=Plantar%20Fasciitis&aggFilters=status%3Arec&checkSpell=true&from=0&limit=10&fields=OverallStatus%2CLastKnownStatus%2CStatusVerifiedDate%2CHasResults%2CBriefTitle%2CCondition%2CInterventionType%2CInterventionName%2CLocationFacility%2CLocationCity%2CLocationState%2CLocationCountry%2CLocationStatus%2CLocationZip%2CLocationGeoPoint%2CLocationContactName%2CLocationContactRole%2CLocationContactPhone%2CLocationContactPhoneExt%2CLocationContactEMail%2CCentralContactName%2CCentralContactRole%2CCentralContactPhone%2CCentralContactPhoneExt%2CCentralContactEMail%2CGender%2CMinimumAge%2CMaximumAge%2CStdAge%2CNCTId%2CStudyType%2CLeadSponsorName%2CAcronym%2CEnrollmentCount%2CStartDate%2CPrimaryCompletionDate%2CCompletionDate%2CStudyFirstPostDate%2CResultsFirstPostDate%2CLastUpdatePostDate%2COrgStudyId%2CSecondaryId%2CPhase%2CLargeDocLabel%2CLargeDocFilename%2CPrimaryOutcomeMeasure%2CSecondaryOutcomeMeasure%2CDesignAllocation%2CDesignInterventionModel%2CDesignMasking%2CDesignWhoMasked%2CDesignPrimaryPurpose%2CDesignObservationalModel%2CDesignTimePerspective%2CLeadSponsorClass%2CCollaboratorClass&columns=conditions%2Cinterventions%2Ccollaborators&highlight=true&sort=%40relevance

grabbed the open api spec for it, and edited it (in swagger editor) to just focus on /studies for now and lower context window

[shortened for /studies endpoint here](ctg-oas-v2.yaml)

generated codegen