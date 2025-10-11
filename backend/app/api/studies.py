from typing import Any, Dict

from fastapi import APIRouter, HTTPException, Query

from app.services.clinical_trials import search_clinical_trials

router = APIRouter()

@router.get("/studies")
def get_studies(
    condition: str = Query(..., description="Condition to search for"),
    page_size: int = Query(10, description="Number of results per page", ge=1, le=100),
    page_token: str = Query(None, description="Token for pagination")
) -> Dict[str, Any]:
    """
    Search for clinical trials by condition.
    
    Args:
        condition: The medical condition to search for
        page_size: Number of results per page (1-100)
        page_token: Token for pagination
        
    Returns:
        Dictionary containing the search results with structure:
        {
            "studies": [...],
            "total_count": int,
            "next_page_token": str or None,
            "metadata": {...}
        }
        
    Raises:
        HTTPException: If the API call fails
    """
    try:
        # Use the clinical trials service
        result = search_clinical_trials(
            condition=condition,
            page_size=page_size,
            page_token=page_token
        )
        
        return result
            
    except RuntimeError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Clinical trials API error: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )
