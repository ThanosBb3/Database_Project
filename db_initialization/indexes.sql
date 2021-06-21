USE HotelDB;
CREATE INDEX visit_time ON visit(enter_datetime, leave_datetime)
CREATE INDEX use_cost ON useService(cost)
CREATE INDEX use_time ON useService(date_time)