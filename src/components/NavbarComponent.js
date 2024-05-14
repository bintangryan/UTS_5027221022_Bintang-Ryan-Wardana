import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { Link } from 'react-router-dom'; // Import Link dari React Router

function NavbarComponent() {
  return (
    <Navbar style={{ backgroundColor: 'black' }} variant="dark" expand="lg">
      <Container>
        <Navbar.Brand as={Link} to="/" style={{ fontWeight: 'bold', color: 'green' }}>Fainens</Navbar.Brand> {/* Gunakan Link untuk navigasi */}
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link as={Link} to="/">Dashboard</Nav.Link> {/* Tautan ke halaman dashboard */}
            <Nav.Link as={Link} to="/history">History</Nav.Link> {/* Tautan ke halaman history */}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavbarComponent;
