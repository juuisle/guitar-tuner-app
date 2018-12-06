import React, { Component } from 'react';
import { Field, reduxForm } from 'redux-form';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { createTuning } from '../actions';

class TuningsNew extends Component {
  renderField(field) {
    const { meta: {touched, error } } = field;
    const className = `form-group ${touched && error ? 'has-danger' : ''}`

    return (
      <div className={className}>
        <label> {field.label} </label>
          <input
            className="form-control"
            type="text"
            {...field.input}
          />
        <div className="text-help"> {touched ? error : ''}</div>
      </div>
    );
  }

  onSubmit(values) {
    this.props.createTuning(values, () => {
      this.props.history.push('/');
    });
  }

  render() {
    const { handleSubmit } = this.props;

    return (
      <form onSubmit={handleSubmit(this.onSubmit.bind(this))}>
        <Field
          label="Tuning Name"
          name="name"
          component={this.renderField}
        />
        <Field
          label="String One"
          name="str_one"
          component={this.renderField}
        />
        <Field
          label="String Two"
          name="str_two"
          component={this.renderField}
        />
        <Field
          label="String Three"
          name="str_three"
          component={this.renderField}
        />
        <Field
          label="String Four"
          name="str_four"
          component={this.renderField}
        />
        <Field
          label="String Five"
          name="str_five"
          component={this.renderField}
        />
        <Field
          label="String Six"
          name="str_six"
          component={this.renderField}
        />
        <button type="submit" className="btn btn-primary"> Save </button>
        <Link className="btn btn-danger" to="/"> Cancel </Link>
      </form>
    );
  };
}
function validate(values) {
  const errors = {};

  // Validate the inputs from 'values'
  if (!values.name) {
    errors.name = "Enter a title";
  }
  if (!values.str_one) {
    errors.str_one = "Enter frequency";
  }
  if (!values.str_two) {
    errors.str_two = "Enter frequency";
  }
  if (!values.str_three) {
    errors.str_three = "Enter frequency";
  }
  if (!values.str_four) {
    errors.str_four = "Enter frequency";
  }
  if (!values.str_five) {
    errors.str_five = "Enter frequency";
  }
  if (!values.str_six) {
    errors.str_six = "Enter frequency";
  }

  return errors;
}

export default reduxForm({
  validate,
  form: 'TuningsNewForm'
})(
  connect(null,{ createTuning })(TuningsNew)
);
