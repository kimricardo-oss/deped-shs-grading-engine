from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
from app.calculator import SubjectGradeEngine

app = FastAPI(title="DepEd SHS Grading Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SingleSubjectRequest(BaseModel):
    subject_name: str
    category: str
    written_works_pct: float = Field(..., ge=0, le=100)
    performance_tasks_pct: float = Field(..., ge=0, le=100)
    quarterly_exam_pct: Optional[float] = Field(0.0, ge=0, le=100)

@app.get("/")
def read_root():
    return {"status": "active", "framework": "DepEd DM 074, s. 2025"}

@app.post("/api/v1/calculate/subject")
def calculate_subject_grade(request: SingleSubjectRequest):
    try:
        result = SubjectGradeEngine.calculate_single_subject(
            category=request.category,
            ww_score=request.written_works_pct,
            pt_score=request.performance_tasks_pct,
            qa_score=request.quarterly_exam_pct
        )
        return {"subject": request.subject_name, "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
