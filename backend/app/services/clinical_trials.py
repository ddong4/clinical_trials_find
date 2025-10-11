"""
Service for interacting with ClinicalTrials.gov API
"""
import logging
from typing import Any, Dict

from openapi_client import ApiClient, Configuration
from openapi_client.api.studies_api import StudiesApi
from openapi_client.models.paged_studies import PagedStudies

# Set up logger
logger = logging.getLogger(__name__)


class ClinicalTrialsService:
    """Service for searching clinical trials using ClinicalTrials.gov API"""
    
    def __init__(self, base_url: str = "https://clinicaltrials.gov/api/v2"):
        """Initialize the clinical trials service"""
        self.base_url = base_url
        self._api_client = None
        self._studies_api = None
    
    @property
    def api_client(self) -> ApiClient:
        """Lazy initialization of API client"""
        if self._api_client is None:
            config = Configuration(host=self.base_url)
            self._api_client = ApiClient(config)
        return self._api_client
    
    @property
    def studies_api(self) -> StudiesApi:
        """Lazy initialization of Studies API"""
        if self._studies_api is None:
            self._studies_api = StudiesApi(self.api_client)
        return self._studies_api
    
    def search_clinical_trials(
        self, condition: str, page_size: int, is_recruiting: bool = False, page_token: str | None = None
    ) -> Dict[str, Any]:
        """
        Search clinical trials by condition
        
        Args:
            condition: Medical condition to search for
            page_size: Number of results per page
            page_token: Token for pagination
            is_recruiting: If True, filter to only recruiting studies (RECRUITING, ENROLLING_BY_INVITATION)
            
        Returns:
            Dictionary containing search results
            
        Raises:
            RuntimeError: If API call fails
        """
        try:
            logger.info(f"Searching clinical trials for condition: {condition}")
            
            # Set up filters
            filter_overall_status = []
            if is_recruiting:
                filter_overall_status = ["RECRUITING", "ENROLLING_BY_INVITATION"]
                logger.info("Filtering to recruiting studies only")
            
            # Perform the search
            response: PagedStudies = self.studies_api.list_studies(
                query_cond=condition,
                page_size=page_size,
                page_token=page_token,
                filter_overall_status=filter_overall_status,
                format="json",
            )
            
            logger.info(f"Successfully retrieved {len(response.studies or [])} studies")
            
            # Convert the response to a dictionary
            return response.to_dict()

        except Exception as e:
            logger.error(f"Error calling ClinicalTrials.gov API: {e}")
            raise RuntimeError(f"Error calling ClinicalTrials.gov API: {e}") from e


# Dependency function to get configured clinical trials service
def get_clinical_trials_service() -> ClinicalTrialsService:
    """Dependency function to get configured ClinicalTrials service"""
    return ClinicalTrialsService()

# Backwards-compatible module-level function used by API layer
def search_clinical_trials(
    condition: str,
    page_size: int,
    page_token: str | None = None,
    is_recruiting: bool = False,
) -> Dict[str, Any]:
    """Convenience wrapper to search clinical trials without managing the service instance."""
    service = ClinicalTrialsService()
    return service.search_clinical_trials(condition=condition, page_size=page_size, page_token=page_token, is_recruiting=is_recruiting)
