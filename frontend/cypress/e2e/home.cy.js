describe("Homepage", () => {
  it("shows success message", () => {
    cy.visit("http://localhost:3000");
    cy.contains("You've successfully integrated the backend!");
  });

  it("displays current backend URL", () => {
    cy.visit("http://localhost:3000");
    cy.contains("Backend URL");
  });
});
