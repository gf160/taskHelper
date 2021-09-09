import os
import pandas as pd
import glob
import log
import time

logger = log.setLogging("excelUtil")

def beforeFolderMerge():
    beforeFileList = os.listdir('./excel_before')

    if len(beforeFileList) == 0:
        logger.warn("excel_before Folder is empty")
    else:
        allBeforeData = pd.DataFrame()
        index = 0
        for file in glob.glob('./excel_before/*.xlsx'):
            df = pd.read_excel(file)
            allBeforeData = allBeforeData.append(df, ignore_index=True)
            logger.info('file read is done --> ' + str(index))
            index += 1

        logger.debug(allBeforeData.shape)
        timeStr = time.strftime("%Y%m%d_%H%M%S")

        allBeforeData.to_excel('./excel_result/before_result_' + timeStr + '.xlsx', index=False)

        logger.info("Before Files Merge Complete")

def afterFolderMerge():
    afterFileList = os.listdir('./excel_after')

    if len(afterFileList) == 0:
        logger.warn("excel_after Folder is empty")
    else:
        allAfterData = pd.DataFrame()
        index = 0
        for file in glob.glob('./excel_after/*.xlsx'):
            df = pd.read_excel(file)
            allAfterData = allAfterData.append(df, ignore_index=True)
            logger.info('file read is done --> ' + str(index))
            index += 1

        logger.debug(allAfterData.shape)
        timeStr = time.strftime("%Y%m%d_%H%M%S")

        allAfterData.to_excel('./excel_result/after_result_' + timeStr + '.xlsx', index=False)

        logger.info("After Files Merge Complete")
