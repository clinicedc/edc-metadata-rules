from dateutil.relativedelta import relativedelta

from edc_visit_schedule import VisitSchedule, Schedule, Visit
from edc_visit_schedule import FormsCollection, Crf, Requisition

app_label = 'edc_metadata_rules'

crfs0 = FormsCollection(
    Crf(show_order=1, model=f'{app_label}.crfone', required=True),
    Crf(show_order=2, model=f'{app_label}.crftwo', required=True),
    Crf(show_order=3, model=f'{app_label}.crfthree', required=True),
    Crf(show_order=4, model=f'{app_label}.crffour', required=True),
    Crf(show_order=5, model=f'{app_label}.crffive', required=True),
)

crfs1 = FormsCollection(
    Crf(show_order=1, model=f'{app_label}.crffour', required=True),
    Crf(show_order=2, model=f'{app_label}.crffive', required=True),
    Crf(show_order=3, model=f'{app_label}.crfsix', required=True),
)

crfs2 = FormsCollection(
    Crf(show_order=1, model=f'{app_label}.crfseven', required=True),
)


requisitions0 = FormsCollection(
    Requisition(
        show_order=10, model=f'{app_label}.subjectrequisition',
        panel='one', required=False, additional=False),
    Requisition(
        show_order=20, model=f'{app_label}.subjectrequisition',
        panel='two', required=False, additional=False),
    Requisition(
        show_order=30, model=f'{app_label}.subjectrequisition',
        panel='three', required=False, additional=False),
    Requisition(
        show_order=40, model=f'{app_label}.subjectrequisition',
        panel='four', required=False, additional=False),
    Requisition(
        show_order=50, model=f'{app_label}.subjectrequisition',
        panel='five', required=False, additional=False),
    Requisition(
        show_order=60, model=f'{app_label}.subjectrequisition',
        panel='six', required=False, additional=False),
)

requisitions1 = FormsCollection(
    Requisition(
        show_order=10, model=f'{app_label}.subjectrequisition',
        panel='four', required=False, additional=False),
    Requisition(
        show_order=20, model=f'{app_label}.subjectrequisition',
        panel='five', required=False, additional=False),
    Requisition(
        show_order=30, model=f'{app_label}.subjectrequisition',
        panel='six', required=False, additional=False),
    Requisition(
        show_order=40, model=f'{app_label}.subjectrequisition',
        panel='seven', required=False, additional=False),
    Requisition(
        show_order=50, model=f'{app_label}.subjectrequisition',
        panel='eight', required=False, additional=False),
    Requisition(
        show_order=60, model=f'{app_label}.subjectrequisition',
        panel='nine', required=False, additional=False),
)


requisitions2 = FormsCollection(
    Requisition(
        show_order=10, model='edc_metadata_rules.subjectrequisition',
        panel='seven', required=False, additional=False),
)

visit0 = Visit(
    code='1000',
    title='Day 1',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions0,
    crfs=crfs0)

visit1 = Visit(
    code='2000',
    title='Day 2',
    timepoint=1,
    rbase=relativedelta(days=1),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions1,
    crfs=crfs1)

visit2 = Visit(
    code='3000',
    title='Day 3',
    timepoint=2,
    rbase=relativedelta(days=2),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions2,
    crfs=crfs2)

schedule = Schedule(
    name='schedule',
    enrollment_model=f'{app_label}.enrollment',
    disenrollment_model=f'{app_label}.disenrollment')

schedule.add_visit(visit0)
schedule.add_visit(visit1)
schedule.add_visit(visit2)

visit_schedule = VisitSchedule(
    name='visit_schedule',
    visit_model=f'{app_label}.subjectvisit',
    offstudy_model=f'{app_label}.subjectoffstudy')

visit_schedule.add_schedule(schedule)
