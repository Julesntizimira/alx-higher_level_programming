# include "lists.h"
/**
 * add_dnodeint - adds a new node at the beginning
 * @head: input head node
 * @n: newnode data
 * Return: new node
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *tmp = *head, *newnode = NULL;

	newnode = malloc(sizeof(dlistint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = n;
	if (*head == NULL)
		*head = newnode;
	else
	{
		tmp->prev = newnode;
		newnode->next = tmp;
		*head = newnode;
	}
	return (newnode);
}
