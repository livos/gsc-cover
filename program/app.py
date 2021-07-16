import os
import zipfile
import shutil
import pandas as pd
from program import log
import program.settings as settings
import inspect
from .data.local.database.db_helper import sessionScope

logger = log.setup(__name__)

def run():
    logger.debug(inspect.stack()[0][3])

    try:
        with sessionScope(settings.DB_CONNECTION_STRING) as session: 
            for file_name in os.listdir(settings.GSC_ZIPS_DIR):
                if file_name.endswith(".zip"):
                    logger.debug("Processing zip : {}".format(file_name))
                    with zipfile.ZipFile(settings.GSC_ZIPS_DIR + file_name,"r") as zf:
                        zf.extractall(settings.GSC_ZIPS_DIR + "tmp")

                        df_metadata = pd.read_csv(settings.GSC_ZIPS_DIR + "tmp/" + "Metadata.csv")
                        status = df_metadata.iloc[1]["Value"]

                        df_data = pd.read_csv(settings.GSC_ZIPS_DIR + "tmp/" + "Table.csv")
                        df_data.columns = df_data.columns.str.lower()
                        df_data["status"] = status.strip()
                        df_data.to_sql("crawls", session.get_bind().connect() , if_exists='append', index = False)
        shutil.rmtree(settings.GSC_ZIPS_DIR + "tmp")
    except:
        logger.exception("Error in {}".format(inspect.stack()[0][3]))

