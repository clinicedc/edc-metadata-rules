from dateutil.relativedelta import relativedelta

from edc_visit_schedule import VisitSchedule, Schedule, Visit
from edc_visit_schedule import FormsCollection, Crf, Requisition

app_label = 'edc_metadata_rules'

crfs = FormsCollection(
    Crf(show_order=1, model=f'{app_label}.crfone', required=True),
    Crf(show_order=2, model=f'{app_label}.crftwo', required=True),
    Crf(show_order=3, model=f'{app_label}.crfthree', required=True),
    Crf(show_order=4, model=f'{app_label}.crffour', required=True),
    Crf(show_order=5, model=f'{app_label}.crffive', required=True),
)

requisitions = FormsCollection(
    Requisition(
        show_order=10, model=f'{app_label}.subjectrequisition',
        panel='one', required=True, additional=False),
    Requisition(
        show_order=20, model=f'{app_label}.subjectrequisition',
        panel='two', required=True, additional=False),
    Requisition(
        show_order=30, model=f'{app_label}.subjectrequisition',
        panel='three', required=True, additional=False),
    Requisition(
        show_order=40, model=f'{app_label}.subjectrequisition',
        panel='four', required=True, additional=False),
    Requisition(
        show_order=50, model=f'{app_label}.subjectrequisition',
        panel='five', required=True, additional=False),
    Requisition(
        show_order=60, model=f'{app_label}.subjectrequisition',
        panel='six', required=True, additional=False),
)

visit0 = Visit(
    code='1000',
    title='Day 1',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crfs)

visit1 = Visit(
    code='2000',
    title='Day 2',
    timepoint=1,
    rbase=relativedelta(days=1),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crfs)

schedule = Schedule(
    name='schedule',
    enrollment_model=f'{app_label}.enrollment',
    disenrollment_model=f'{app_label}.disenrollment')

schedule.add_visit(visit0)
schedule.add_visit(visit1)

visit_schedule = VisitSchedule(
    name='visit_schedule',
    visit_model=f'{app_label}.subjectvisit',
    offstudy_model=f'{app_label}.subjectoffstudy')

visit_schedule.add_schedule(schedule)
