SELECT outs.ANIMAL_ID as ANIMAL_ID, outs.NAME as NAME
from ANIMAL_OUTS outs
left join ANIMAL_INS ins on outs.ANIMAL_ID = ins.ANIMAL_ID
where ins.INTAKE_CONDITION is null