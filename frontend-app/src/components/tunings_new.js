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
  if(values.name.length > 18) {
	errors.name = "Name has to be maximum of 18 characters."
  }
  
  if (!values.str_one) {
    errors.str_one = "Enter frequency";
  }
  if (values.str_one <==112.00 && values.str_one ==>70.00) {
    errors.str_one = "Frequency out of range";
  }
  
  if (!values.str_two) {
    errors.str_two = "Enter frequency";
  }
  if (values.str_two <==140.00 && values.str_two ==>90.00) {
    errors.str_two = "Frequency out of range";
  }
  
  if (!values.str_three) {
    errors.str_three = "Enter frequency";
  }
  if (values.str_three <==176.00 && values.str_three ==>116.00) {
    errors.str_three = "Frequency out of range";
  }
  
  if (!values.str_four) {
    errors.str_four = "Enter frequency";
  }
  if (values.str_four <==226.00 && values.str_four ==>166.00) {
    errors.str_four = "Frequency out of range";
  }
  
  if (!values.str_five) {
    errors.str_five = "Enter frequency";
  }
  if (values.str_five <==276.00 && values.str_five ==>216.00) {
    errors.str_five = "Frequency out of range";
  }
  
  if (!values.str_six) {
    errors.str_six = "Enter frequency";
  }
  if (values.str_five <==360.00 && values.str_five ==>300.00) {
    errors.str_five = "Frequency out of range";
  }

  return errors;
}

export default reduxForm({
  validate,
  form: 'TuningsNewForm'
})(
  connect(null,{ createTuning })(TuningsNew)
);
