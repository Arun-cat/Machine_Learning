from pydantic import BaseModel

class HeartInput(BaseModel):
    Age: int
    Sex_M: int
    ChestPainType_ATA: int
    ChestPainType_NAP:int
    ChestPainType_TA:int
    RestingECG_Normal:int
    RestingECG_ST:int
    Cholesterol: int
    FastingBS: int
    RestingECG: int
    MaxHR: int
    ExerciseAngina_Y: int
    Oldpeak: float
    ST_Slope_Flat:int
    ST_Slope_Up:int