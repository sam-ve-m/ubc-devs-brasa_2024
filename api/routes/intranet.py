from fastapi import APIRouter, Depends

from api.services.dump import dump_example_files_into_mongo
from api.routes.dependencies import get_m_c_c_repository, get_sales_repository, get_bank_repository
from api.repositories.bank import BankRepository
from api.repositories.mcc import MCCRepository
from api.repositories.sales import SalesRepository

router = APIRouter()


@router.post("/database_dump")
def database_dump(
        sales_repository: SalesRepository = Depends(get_sales_repository),
        bank_repository: BankRepository = Depends(get_bank_repository),
        mcc_repository: MCCRepository = Depends(get_m_c_c_repository),
):
    return dump_example_files_into_mongo(
        sales_repository,
        bank_repository,
        mcc_repository
    )


__all__ = router,
