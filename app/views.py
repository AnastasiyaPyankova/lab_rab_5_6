from flask import Blueprint, request

from app import db
from app.models import Employee, Position, Division, Job

bp = Blueprint('bp', __name__)


# Запросы для Employee


@bp.route('/employee/add', methods=['POST'])
def add_employee():
    employee = Employee(**request.args)
    db.session.add(employee)
    db.session.commit()
    return employee.to_dict()


@bp.route('/employee/delete', methods=['DELETE'])
def delete_employee():
    employee = Employee.query.get(request.args.get('id'))
    db.session.delete(employee)
    db.session.commit()
    return employee.to_dict()


@bp.route('/employee/put', methods=['PUT'])
def put_employee():
    employee = Employee.query.get(request.args.get('id'))
    if request.args.get('surname'):
        employee.second_name = request.args.get('surname')
    if request.args.get('name'):
        employee.first_name = request.args.get('name')
    if request.args.get('patronymic'):
        employee.surname = request.args.get('patronymic')
    if request.args.get('address'):
        employee.address = request.args.get('address')
    if request.args.get('date_of_birth'):
        employee.date_of_birth = request.args.get('date_of_birth')
    db.session.add(employee)
    db.session.commit()
    return employee.to_dict()


@bp.route('/employee/get', methods=['GET'])
def get_employee():
    employee = Employee.query.get(request.args.get('id'))
    return employee.to_dict()


# Запросы для Position


@bp.route('/position/add', methods=['POST'])
def add_position():
    position = Position(**request.args)
    db.session.add(position)
    db.session.commit()
    return position.to_dict()


@bp.route('/position/delete', methods=['DELETE'])
def delete_position():
    position = Position.query.get(request.args.get('id'))
    db.session.delete(position)
    db.session.commit()
    return position.to_dict()


@bp.route('/position/get', methods=['GET'])
def get_position():
    position = Position.query.get(request.args.get('id'))
    return position.to_dict()


# Запросы для Division


@bp.route('/division/add', methods=['POST'])
def add_division():
    division = Division(**request.args)
    db.session.add(division)
    db.session.commit()
    return division.to_dict()


@bp.route('/division/delete', methods=['DELETE'])
def delete_division():
    division = Division.query.get(request.args.get('id'))
    db.session.delete(division)
    db.session.commit()
    return division.to_dict()


@bp.route('/division/get', methods=['GET'])
def get_division():
    division = Division.query.get(request.args.get('id'))
    return division.to_dict()


# Устройство сотрудника

@bp.route('/job/add', methods=['POST'])
def add_job():
    employ = Employee.query.get(request.args.get('employee_id'))
    pos = Position.query.get(request.args.get('position_id'))
    div = Division.query.get(request.args.get('division_id'))
    data_job = {
        "employee_id": employ.id,
        "position_id": pos.id,
        "division_id": div.id,
        "date_of_employment": request.args.get('date_of_employment'),
    }
    job = Job(**data_job)
    db.session.add(job)
    db.session.commit()
    return job.to_dict()


# Увольнение сотрудника

@bp.route('/job/delete', methods=['PUT'])
def delete_job():
    job = Job.query.get(request.args.get('id'))
    job.date_of_dismissal = request.args.get('date_of_dismissal')
    db.session.add(job)
    db.session.commit()
    return job.to_dict()


# Получение списка устроенных

@bp.route('/job/get', methods=['GET'])
def get_list_of_employees():
    jobs = Employee.query.join(Job).order_by(Job.date_of_employment)
    if request.args.get('division_id'):
        jobs = jobs.filter(Job.division_id == request.args.get('division_id'))
    elif request.args.get('sort_after_date'):
        jobs = jobs.filter(Job.date_of_employment > request.args.get('sort_after_date'))
    jobs = jobs.all()
    list_of_employees = [job.to_dict() for job in jobs]
    return list_of_employees
