from app.logger import log


def client_func(*args):
    log(log.INFO, "Client func start")
    log(log.INFO, "Args: [%s]", args)
    from client_script.pulling_from_stockx import (
        all,
        DS_condition,
        SDS_condition,
        LW_condition,
        MW_condition,
        HW_condition,
        RB_condition,
        BG_condition,
        SLW_condition,
        SMW_condition,
        SHW_condition,
    )
    from app.models import Input
    input1 = Input.query.filter(Input.name == "value1").first()
    input2 = Input.query.filter(Input.name == "value2").first()
    input3 = Input.query.filter(Input.name == "value3").first()
    input4 = Input.query.filter(Input.name == "value4").first()
    input5 = Input.query.filter(Input.name == "value5").first()
    input6 = Input.query.filter(Input.name == "value6").first()
    input7 = Input.query.filter(Input.name == "value7").first()
    input8 = Input.query.filter(Input.name == "value8").first()
    input9 = Input.query.filter(Input.name == "value9").first()
    input10 = Input.query.filter(Input.name == "value10").first()

    DS_condition = input1.value
    SDS_condition = input2.value
    LW_condition = input3.value
    MW_condition = input4.value
    HW_condition = input5.value
    RB_condition = input6.value
    BG_condition = input7.value
    SLW_condition = input8.value
    SMW_condition = input9.value
    SHW_condition = input10.value
    all()
