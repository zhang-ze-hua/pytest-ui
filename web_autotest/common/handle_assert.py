from common.handle_logging import log


def handle_assert(expected, result, case_type, title, case_id, column, excel):
    try:
        assert expected == result
    except AssertionError as e:
        if result is None:
            log.warning("{}==={}===未执行".format(case_type, title))
            excel.write_data(row=case_id + 1, column=column, value="未执行")
        else:
            log.error("{}==={}===执行不通过".format(case_type, title))
            log.debug("实际结果：{}".format(result))
            log.debug("预期结果：{}".format(expected))
            log.exception(e)
            excel.write_data(row=case_id + 1, column=column, value="不通过")
            raise e
    else:
        log.info("{}==={}===执行通过".format(case_type, title))
        log.debug("实际结果：{}".format(result))
        log.debug("预期结果：{}".format(expected))
        excel.write_data(row=case_id + 1, column=column, value="通过")
