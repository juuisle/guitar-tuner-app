import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import { fetchTuning, deleteTuning, selectTuning } from '../actions';


class TuningsShow extends Component {
  componentDidMount() {
      const { id } = this.props.match.params;
      this.props.fetchTuning(id);
  }

  onDeleteClick() {
    const { id } = this.props.match.params;
    this.props.deleteTuning(id, () => {
      this.props.history.push("/");
    });
  }

  onSelectClick() {
    const { id } = this.props.match.params;
    this.props.selectTuning(id, () => {
    this.props.history.push('/');
    });
  }

  render() {
    const { tuning } = this.props;
    if (!tuning) {
      return <div> Loading...</div>
    } else {
      return (
        <div>
        <Link to="/">Back To INDEX</Link>
        <button
          className="btn btn-danger pull-xs-right"
          onClick={this.onDeleteClick.bind(this)}
        >
          Delete Tuning
        </button>

        <h3>Detail of {tuning.name}</h3>
        <p>String One: {tuning.str_one} Hz</p>
        <p>String Two: {tuning.str_two} Hz</p>
        <p>String Three: {tuning.str_three} Hz</p>
        <p>String Four: {tuning.str_four} Hz</p>
        <p>String Five: {tuning.str_five} Hz</p>
        <p>String Six: {tuning.str_six} Hz</p>

        <button
        className="btn pull-xs-right"
        onClick={this.onSelectClick.bind(this)}
        >
        Select this Tuning for my Guitar
        </button>
        </div>
      );
    }
  }
}

function mapStateToProps({ tunings }, ownProps) {
  return { tuning: tunings[ownProps.match.params.id] };
}

export default connect(mapStateToProps, { fetchTuning, deleteTuning, selectTuning })(TuningsShow);
