# openapi_client.StudiesApi

All URIs are relative to *https://clinicaltrials.gov/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_studies**](StudiesApi.md#list_studies) | **GET** /studies | Studies


# **list_studies**
> PagedStudies list_studies(format=format, markup_format=markup_format, query_cond=query_cond, query_term=query_term, query_locn=query_locn, query_titles=query_titles, query_intr=query_intr, query_outc=query_outc, query_spons=query_spons, query_lead=query_lead, query_id=query_id, query_patient=query_patient, filter_overall_status=filter_overall_status, filter_geo=filter_geo, filter_ids=filter_ids, filter_advanced=filter_advanced, filter_synonyms=filter_synonyms, post_filter_overall_status=post_filter_overall_status, post_filter_geo=post_filter_geo, post_filter_ids=post_filter_ids, post_filter_advanced=post_filter_advanced, post_filter_synonyms=post_filter_synonyms, agg_filters=agg_filters, geo_decay=geo_decay, fields=fields, sort=sort, count_total=count_total, page_size=page_size, page_token=page_token)

Studies

Returns data of studies matching query and filter parameters. The studies are returned page by page.
If response contains `nextPageToken`, use its value in `pageToken` to get next page.
The last page will not contain `nextPageToken`. A page may have empty `studies` array.
Request for each subsequent page **must** have the same parameters as for the first page, except
`countTotal`, `pageSize`, and `pageToken` parameters.

If neither queries nor filters are set, all studies will be returned.
If any query parameter contains only NCT IDs (comma- and/or space-separated), filters are ignored.

`query.*` parameters are in [Essie expression syntax](/find-studies/constructing-complex-search-queries).
Those parameters affect ranking of studies, if sorted by relevance. See `sort` parameter for details.

`filter.*` and `postFilter.*` parameters have same effect as there is no aggregation calculation. 
Both are available just to simplify applying parameters from search request.
Both do not affect ranking of studies.

Note: When trying JSON format in your browser, do not set too large `pageSize` parameter, if `fields` is
unlimited. That may return too much data for the browser to parse and render.

### Example


```python
import openapi_client
from openapi_client.models.paged_studies import PagedStudies
from openapi_client.models.status import Status
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://clinicaltrials.gov/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://clinicaltrials.gov/api/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StudiesApi(api_client)
    format = json # str | Must be one of the following: * `csv`- return CSV table with one page of study data; first page will contain header with column names; available fields are listed on [CSV Download](/data-api/about-api/csv-download) page * `json`- return JSON with one page of study data; every study object is placed in a separate line; `markup` type fields format depends on `markupFormat` parameter (optional) (default to json)
    markup_format = markdown # str | Format of `markup` type fields: * `markdown`- [markdown](https://spec.commonmark.org/0.28/) format * `legacy`- compatible with classic PRS  Applicable only to `json` format. (optional) (default to markdown)
    query_cond = 'lung cancer' # str | \"Conditions or disease\" query in [Essie expression syntax](/find-studies/constructing-complex-search-queries). See \"ConditionSearch Area\" on [Search Areas](/data-api/about-api/search-areas#ConditionSearch) for more details. (optional)
    query_term = 'AREA[LastUpdatePostDate]RANGE[2023-01-15,MAX]' # str | \"Other terms\" query in [Essie expression syntax](/find-studies/constructing-complex-search-queries). See \"BasicSearch Area\" on [Search Areas](/data-api/about-api/search-areas#BasicSearch) for more details. (optional)
    query_locn = 'query_locn_example' # str | \"Location terms\" query in [Essie expression syntax](/find-studies/constructing-complex-search-queries). See \"LocationSearch Area\" on [Search Areas](/data-api/about-api/search-areas#LocationSearch) for more details. (optional)
    query_titles = 'query_titles_example' # str | \"Title / acronym\" query in [Essie expression syntax](/find-studies/constructing-complex-search-queries). See \"TitleSearch Area\" on [Search Areas](/data-api/about-api/search-areas#TitleSearch) for more details. (optional)
    query_intr = 'query_intr_example' # str | \"Intervention / treatment\" query in [Essie expression syntax](/find-studies/constructing-complex-search-queries). See \"InterventionSearch Area\" on [Search Areas](/data-api/about-api/search-areas#InterventionSearch) for more details. (optional)
    query_outc = 'query_outc_example' # str | \"Outcome measure\" query in [Essie expression syntax](/find-studies/constructing-complex-search-queries). See \"OutcomeSearch Area\" on [Search Areas](/data-api/about-api/search-areas#OutcomeSearch) for more details. (optional)
    query_spons = 'query_spons_example' # str | \"Sponsor / collaborator\" query in [Essie expression syntax](/find-studies/constructing-complex-search-queries). See \"SponsorSearch Area\" on [Search Areas](/data-api/about-api/search-areas#SponsorSearch) for more details. (optional)
    query_lead = 'query_lead_example' # str | Searches in \"LeadSponsorName\" field. See [Study Data Structure](/data-api/about-api/study-data-structure#LeadSponsorName) for more details. The query is in [Essie expression syntax](/find-studies/constructing-complex-search-queries). (optional)
    query_id = 'query_id_example' # str | \"Study IDs\" query in [Essie expression syntax](/find-studies/constructing-complex-search-queries). See \"IdSearch Area\" on [Search Areas](/data-api/about-api/search-areas#IdSearch) for more details. (optional)
    query_patient = 'query_patient_example' # str | See \"PatientSearch Area\" on [Search Areas](/data-api/about-api/search-areas#PatientSearch) for more details. (optional)
    filter_overall_status = [openapi_client.Status()] # List[Status] | Filter by comma- or pipe-separated list of statuses (optional)
    filter_geo = 'distance(39.0035707,-77.1013313,50mi)' # str | Filter by geo-function. Currently only distance function is supported. Format: `distance(latitude,longitude,distance)` (optional)
    filter_ids = ['[\"NCT04852770\",\"NCT01728545\",\"NCT02109302\"]'] # List[str] | Filter by comma- or pipe-separated list of NCT IDs (a.k.a. ClinicalTrials.gov identifiers). The provided IDs will be searched in [NCTId](data-api/about-api/study-data-structure#NCTId) and [NCTIdAlias](data-api/about-api/study-data-structure#NCTIdAlias) fields. (optional)
    filter_advanced = 'AREA[StartDate]2022' # str | Filter by query in [Essie expression syntax](/find-studies/constructing-complex-search-queries) (optional)
    filter_synonyms = ['[\"ConditionSearch:1651367\",\"BasicSearch:2013558\"]'] # List[str] | Filter by comma- or pipe-separated list of `area`:`synonym_id` pairs (optional)
    post_filter_overall_status = [openapi_client.Status()] # List[Status] | Filter by comma- or pipe-separated list of statuses (optional)
    post_filter_geo = 'distance(39.0035707,-77.1013313,50mi)' # str | Filter by geo-function. Currently only distance function is supported. Format: `distance(latitude,longitude,distance)` (optional)
    post_filter_ids = ['[\"NCT04852770\",\"NCT01728545\",\"NCT02109302\"]'] # List[str] | Filter by comma- or pipe-separated list of NCT IDs (a.k.a. ClinicalTrials.gov identifiers). The provided IDs will be searched in [NCTId](data-api/about-api/study-data-structure#NCTId) and [NCTIdAlias](data-api/about-api/study-data-structure#NCTIdAlias) fields. (optional)
    post_filter_advanced = 'AREA[StartDate]2022' # str | Filter by query in [Essie expression syntax](/find-studies/constructing-complex-search-queries) (optional)
    post_filter_synonyms = ['[\"ConditionSearch:1651367\",\"BasicSearch:2013558\"]'] # List[str] | Filter by comma- or pipe-separated list of `area`:`synonym_id` pairs (optional)
    agg_filters = 'results:with,status:com' # str | Apply aggregation filters, aggregation counts will not be provided. The value is comma- or pipe-separated list of pairs `filter_id`:`space-separated list of option keys` for the checked options. (optional)
    geo_decay = 'func:exp,scale:300mi,offset:0mi,decay:0.5' # str | Set proximity factor by distance from `filter.geo` location to the closest [LocationGeoPoint](/data-api/about-api/study-data-structure#LocationGeoPoint) of a study. Ignored, if `filter.geo` parameter is not set or response contains more than 10,000 studies. (optional) (default to 'func:exp,scale:300mi,offset:0mi,decay:0.5')
    fields = ['[\"NCTId\",\"BriefTitle\",\"OverallStatus\",\"HasResults\"]'] # List[str] | If specified, must be non-empty comma- or pipe-separated list of fields to return. If unspecified, all fields will be returned. Order of the fields does not matter.  For `csv` format, specify list of columns. The column names are available on [CSV Download](/data-api/about-api/csv-download).  For `json` format, every list item is either area name, piece name, field name, or special name. If a piece or a field is a branch node, all descendant fields will be included. All area names are available on [Search Areas](/data-api/about-api/search-areas), the piece and field names — on [Data Structure](/data-api/about-api/study-data-structure) and also can be retrieved at `/studies/metadata` endpoint. There is a special name, `@query`, which expands to all fields queried by search. (optional)
    sort = [] # List[str] | Comma- or pipe-separated list of sorting options of the studies. The returning studies are not sorted by default for a performance reason. Every list item contains a field/piece name and an optional sort direction (`asc` for ascending or `desc` for descending) after colon character.  All piece and field names can be found on [Data Structure](/data-api/about-api/study-data-structure) and also can be retrieved at `/studies/metadata` endpoint. Currently, only date and numeric fields are allowed for sorting. There is a special \"field\" `@relevance` to sort by relevance to a search query.  Studies missing sort field are always last. Default sort direction: * Date field - `desc` * Numeric field - `asc` * `@relevance` - `desc` (optional) (default to [])
    count_total = False # bool | Count total number of studies in all pages and return `totalCount` field with first page, if `true`. For CSV, the result can be found in `x-total-count` response header. The parameter is ignored for the subsequent pages. (optional) (default to False)
    page_size = 10 # int | Page size is maximum number of studies to return in response. It does not have to be the same for every page. If not specified or set to 0, the default value will be used. It will be coerced down to  1,000, if greater than that. (optional) (default to 10)
    page_token = 'page_token_example' # str | Token to get next page. Set it to a `nextPageToken` value returned with the previous page in JSON format. For CSV, it can be found in `x-next-page-token` response header. Do not specify it for first page. (optional)

    try:
        # Studies
        api_response = api_instance.list_studies(format=format, markup_format=markup_format, query_cond=query_cond, query_term=query_term, query_locn=query_locn, query_titles=query_titles, query_intr=query_intr, query_outc=query_outc, query_spons=query_spons, query_lead=query_lead, query_id=query_id, query_patient=query_patient, filter_overall_status=filter_overall_status, filter_geo=filter_geo, filter_ids=filter_ids, filter_advanced=filter_advanced, filter_synonyms=filter_synonyms, post_filter_overall_status=post_filter_overall_status, post_filter_geo=post_filter_geo, post_filter_ids=post_filter_ids, post_filter_advanced=post_filter_advanced, post_filter_synonyms=post_filter_synonyms, agg_filters=agg_filters, geo_decay=geo_decay, fields=fields, sort=sort, count_total=count_total, page_size=page_size, page_token=page_token)
        print("The response of StudiesApi->list_studies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudiesApi->list_studies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Must be one of the following: * &#x60;csv&#x60;- return CSV table with one page of study data; first page will contain header with column names; available fields are listed on [CSV Download](/data-api/about-api/csv-download) page * &#x60;json&#x60;- return JSON with one page of study data; every study object is placed in a separate line; &#x60;markup&#x60; type fields format depends on &#x60;markupFormat&#x60; parameter | [optional] [default to json]
 **markup_format** | **str**| Format of &#x60;markup&#x60; type fields: * &#x60;markdown&#x60;- [markdown](https://spec.commonmark.org/0.28/) format * &#x60;legacy&#x60;- compatible with classic PRS  Applicable only to &#x60;json&#x60; format. | [optional] [default to markdown]
 **query_cond** | **str**| \&quot;Conditions or disease\&quot; query in [Essie expression syntax](/find-studies/constructing-complex-search-queries). See \&quot;ConditionSearch Area\&quot; on [Search Areas](/data-api/about-api/search-areas#ConditionSearch) for more details. | [optional] 
 **query_term** | **str**| \&quot;Other terms\&quot; query in [Essie expression syntax](/find-studies/constructing-complex-search-queries). See \&quot;BasicSearch Area\&quot; on [Search Areas](/data-api/about-api/search-areas#BasicSearch) for more details. | [optional] 
 **query_locn** | **str**| \&quot;Location terms\&quot; query in [Essie expression syntax](/find-studies/constructing-complex-search-queries). See \&quot;LocationSearch Area\&quot; on [Search Areas](/data-api/about-api/search-areas#LocationSearch) for more details. | [optional] 
 **query_titles** | **str**| \&quot;Title / acronym\&quot; query in [Essie expression syntax](/find-studies/constructing-complex-search-queries). See \&quot;TitleSearch Area\&quot; on [Search Areas](/data-api/about-api/search-areas#TitleSearch) for more details. | [optional] 
 **query_intr** | **str**| \&quot;Intervention / treatment\&quot; query in [Essie expression syntax](/find-studies/constructing-complex-search-queries). See \&quot;InterventionSearch Area\&quot; on [Search Areas](/data-api/about-api/search-areas#InterventionSearch) for more details. | [optional] 
 **query_outc** | **str**| \&quot;Outcome measure\&quot; query in [Essie expression syntax](/find-studies/constructing-complex-search-queries). See \&quot;OutcomeSearch Area\&quot; on [Search Areas](/data-api/about-api/search-areas#OutcomeSearch) for more details. | [optional] 
 **query_spons** | **str**| \&quot;Sponsor / collaborator\&quot; query in [Essie expression syntax](/find-studies/constructing-complex-search-queries). See \&quot;SponsorSearch Area\&quot; on [Search Areas](/data-api/about-api/search-areas#SponsorSearch) for more details. | [optional] 
 **query_lead** | **str**| Searches in \&quot;LeadSponsorName\&quot; field. See [Study Data Structure](/data-api/about-api/study-data-structure#LeadSponsorName) for more details. The query is in [Essie expression syntax](/find-studies/constructing-complex-search-queries). | [optional] 
 **query_id** | **str**| \&quot;Study IDs\&quot; query in [Essie expression syntax](/find-studies/constructing-complex-search-queries). See \&quot;IdSearch Area\&quot; on [Search Areas](/data-api/about-api/search-areas#IdSearch) for more details. | [optional] 
 **query_patient** | **str**| See \&quot;PatientSearch Area\&quot; on [Search Areas](/data-api/about-api/search-areas#PatientSearch) for more details. | [optional] 
 **filter_overall_status** | [**List[Status]**](Status.md)| Filter by comma- or pipe-separated list of statuses | [optional] 
 **filter_geo** | **str**| Filter by geo-function. Currently only distance function is supported. Format: &#x60;distance(latitude,longitude,distance)&#x60; | [optional] 
 **filter_ids** | [**List[str]**](str.md)| Filter by comma- or pipe-separated list of NCT IDs (a.k.a. ClinicalTrials.gov identifiers). The provided IDs will be searched in [NCTId](data-api/about-api/study-data-structure#NCTId) and [NCTIdAlias](data-api/about-api/study-data-structure#NCTIdAlias) fields. | [optional] 
 **filter_advanced** | **str**| Filter by query in [Essie expression syntax](/find-studies/constructing-complex-search-queries) | [optional] 
 **filter_synonyms** | [**List[str]**](str.md)| Filter by comma- or pipe-separated list of &#x60;area&#x60;:&#x60;synonym_id&#x60; pairs | [optional] 
 **post_filter_overall_status** | [**List[Status]**](Status.md)| Filter by comma- or pipe-separated list of statuses | [optional] 
 **post_filter_geo** | **str**| Filter by geo-function. Currently only distance function is supported. Format: &#x60;distance(latitude,longitude,distance)&#x60; | [optional] 
 **post_filter_ids** | [**List[str]**](str.md)| Filter by comma- or pipe-separated list of NCT IDs (a.k.a. ClinicalTrials.gov identifiers). The provided IDs will be searched in [NCTId](data-api/about-api/study-data-structure#NCTId) and [NCTIdAlias](data-api/about-api/study-data-structure#NCTIdAlias) fields. | [optional] 
 **post_filter_advanced** | **str**| Filter by query in [Essie expression syntax](/find-studies/constructing-complex-search-queries) | [optional] 
 **post_filter_synonyms** | [**List[str]**](str.md)| Filter by comma- or pipe-separated list of &#x60;area&#x60;:&#x60;synonym_id&#x60; pairs | [optional] 
 **agg_filters** | **str**| Apply aggregation filters, aggregation counts will not be provided. The value is comma- or pipe-separated list of pairs &#x60;filter_id&#x60;:&#x60;space-separated list of option keys&#x60; for the checked options. | [optional] 
 **geo_decay** | **str**| Set proximity factor by distance from &#x60;filter.geo&#x60; location to the closest [LocationGeoPoint](/data-api/about-api/study-data-structure#LocationGeoPoint) of a study. Ignored, if &#x60;filter.geo&#x60; parameter is not set or response contains more than 10,000 studies. | [optional] [default to &#39;func:exp,scale:300mi,offset:0mi,decay:0.5&#39;]
 **fields** | [**List[str]**](str.md)| If specified, must be non-empty comma- or pipe-separated list of fields to return. If unspecified, all fields will be returned. Order of the fields does not matter.  For &#x60;csv&#x60; format, specify list of columns. The column names are available on [CSV Download](/data-api/about-api/csv-download).  For &#x60;json&#x60; format, every list item is either area name, piece name, field name, or special name. If a piece or a field is a branch node, all descendant fields will be included. All area names are available on [Search Areas](/data-api/about-api/search-areas), the piece and field names — on [Data Structure](/data-api/about-api/study-data-structure) and also can be retrieved at &#x60;/studies/metadata&#x60; endpoint. There is a special name, &#x60;@query&#x60;, which expands to all fields queried by search. | [optional] 
 **sort** | [**List[str]**](str.md)| Comma- or pipe-separated list of sorting options of the studies. The returning studies are not sorted by default for a performance reason. Every list item contains a field/piece name and an optional sort direction (&#x60;asc&#x60; for ascending or &#x60;desc&#x60; for descending) after colon character.  All piece and field names can be found on [Data Structure](/data-api/about-api/study-data-structure) and also can be retrieved at &#x60;/studies/metadata&#x60; endpoint. Currently, only date and numeric fields are allowed for sorting. There is a special \&quot;field\&quot; &#x60;@relevance&#x60; to sort by relevance to a search query.  Studies missing sort field are always last. Default sort direction: * Date field - &#x60;desc&#x60; * Numeric field - &#x60;asc&#x60; * &#x60;@relevance&#x60; - &#x60;desc&#x60; | [optional] [default to []]
 **count_total** | **bool**| Count total number of studies in all pages and return &#x60;totalCount&#x60; field with first page, if &#x60;true&#x60;. For CSV, the result can be found in &#x60;x-total-count&#x60; response header. The parameter is ignored for the subsequent pages. | [optional] [default to False]
 **page_size** | **int**| Page size is maximum number of studies to return in response. It does not have to be the same for every page. If not specified or set to 0, the default value will be used. It will be coerced down to  1,000, if greater than that. | [optional] [default to 10]
 **page_token** | **str**| Token to get next page. Set it to a &#x60;nextPageToken&#x60; value returned with the previous page in JSON format. For CSV, it can be found in &#x60;x-next-page-token&#x60; response header. Do not specify it for first page. | [optional] 

### Return type

[**PagedStudies**](PagedStudies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

