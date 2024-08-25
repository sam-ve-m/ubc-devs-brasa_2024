import gdown
import os
import pandas as pd

from api.routes.dependencies import get_m_c_c_repository, get_sales_repository, get_bank_repository
from api.repositories.bank import BankRepository
from api.repositories.mcc import MCCRepository
from api.repositories.sales import SalesRepository


def dump_example_files_into_mongo(
        sales_repository: SalesRepository,
        bank_repository: BankRepository,
        mcc_repository: MCCRepository,
):
    data = {
        'bank': "1dzL_SWBkBs5xrUxuGQTm04oe3USgkL9u",    # banking data
        'sales': "1QK-VgSU3AxXUw330KjYFUj8S9hzKJsG6",   # sales data
        'mcc': "1JN0bR84sgZ_o4wjKPBUmz45NeEEkVgt7",     # mcc description
    }
    repositories = {
        'bank': bank_repository,  # banking data
        'sales': sales_repository,  # sales data
        'mcc': mcc_repository,  # mcc description
    }

    for name, file_id in data.items():
        repository = repositories[name]
        if repository.is_empty():
            gdown.download(f'https://drive.google.com/uc?id={file_id}', name + '.parquet', quiet=False)
            data = pd.read_parquet(name + '.parquet').to_dict('records')
            repository.create_many(data)
            os.remove(name + '.parquet')


if __name__ == "__main__":
    dump_example_files_into_mongo(
        get_sales_repository(),
        get_bank_repository(),
        get_m_c_c_repository()
    )
