import React from 'react';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';

class WorkspaceItem extends React.Component {
  render() {
    return (
      <div>
        <h1>{this.props.name}</h1>
        <List component="nav">
          {this.props.values.map(value => (
            <ListItem button key={value}>
              <ListItemText primary={value}/>
            </ListItem>
          ))}
        </List>
      </div>
    );
  }
}

export default WorkspaceItem;

