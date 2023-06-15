# include "lists.h"
/**
 * add_dnodeint_end- adds a new node at the end
 * @head: input head node
 * @n: newnode data
 * Return: new node
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *tmp = *head;
	dlistint_t *newnode = malloc(sizeof(dlistint_t));
	
	if (newnode == NULL)
		return (NULL);
	newnode->n = n;
	if (*head == NULL || head == NULL)
		*head = newnode;
	else
	{
		tmp = *head;
		while (tmp->next != NULL)
		{
			tmp = tmp->next;
		}
		tmp->next = newnode;
		newnode->prev = tmp;
	}
	return (newnode);
}
