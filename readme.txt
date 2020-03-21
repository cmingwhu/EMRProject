# 血培养项目 参数设置
python dataPre_LisItem_Segmentation.py -i XPY01P.xlsx

python dataPre_BloodCulture_lable.py -i XPY01P.xlsx -f True

python dataPre_dataSynthe.py -m Random -i XPY01P--BCu.xlsx -r XPY01P--BRe.xlsx -p XPY01P--PCT.xlsx -c XPY01P--CRP.xlsx -ha XPY01P--HA.xlsx

