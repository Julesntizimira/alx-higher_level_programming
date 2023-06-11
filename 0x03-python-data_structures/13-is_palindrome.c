# include "lists.h"
/**
 * list_len - compute list len
 * @head: pointer to head of list
 * Return: list length
 */
int list_len(listint_t *head)
{
	listint_t *tmp = head;
	int count = 0;

	while (tmp != NULL)
	{
		count++;
		tmp = tmp->next;
	}
	return (count);
}
/**
 * is_palindrome - check for palindrome
 * @head: pointer to head of list
 * Return: 1 if the list is palindrome or 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int len = 0,  i = 0, *temp;
	int *ptr = NULL, *p;

	if (*head == NULL || head == NULL)
		return (1);
	if (list_len(tmp) == 1)
		return (1);
	len = list_len(tmp);
	ptr = malloc(len * sizeof(int));
	if (ptr == NULL)
		return (0);
	for (i = 0; i < len; i++)
	{
		ptr[i] = tmp->n;
		tmp = tmp->next;
	}
	temp = &ptr[len - 1];
	p = &ptr[0];
	while (p < temp)
	{
		if (*p != *temp)
		{
			free(ptr);
			return (0);
		}
		p++;
		temp--;
	}
	free(ptr);
	return (1);
}
